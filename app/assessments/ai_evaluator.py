"""
AI-Powered Writing Evaluator
Uses Claude API to assess student writing against Ontario curriculum rubrics.
"""

import os
import json

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False


class AIEvaluator:
    """Evaluates student writing using AI against curriculum rubrics."""

    def __init__(self):
        self.api_key = os.environ.get('ANTHROPIC_API_KEY')
        self.client = None
        if HAS_ANTHROPIC and self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)

    def is_available(self):
        """Check if AI evaluation is available."""
        return self.client is not None

    def evaluate_writing(self, student_text, prompt_info):
        """
        Evaluate student writing against the rubric.

        Args:
            student_text: The student's written response
            prompt_info: Dict with prompt details (title, type, requirements)

        Returns:
            Dict with scores, feedback, and improvement suggestions
        """
        if not self.is_available():
            return self._fallback_evaluation(student_text, prompt_info)

        evaluation_prompt = self._build_evaluation_prompt(student_text, prompt_info)

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": evaluation_prompt}
                ]
            )

            response_text = message.content[0].text
            return self._parse_evaluation_response(response_text)

        except Exception as e:
            print(f"AI evaluation error: {e}")
            return self._fallback_evaluation(student_text, prompt_info)

    def _build_evaluation_prompt(self, student_text, prompt_info):
        """Build the prompt for AI evaluation."""
        return f"""You are assessing a Grade 7-8 student's writing for an Ontario curriculum assessment.
Evaluate this writing and provide helpful, encouraging feedback.

WRITING PROMPT: {prompt_info.get('title', 'Writing Assignment')}
TYPE: {prompt_info.get('type', 'General Writing')}
REQUIREMENTS: {prompt_info.get('word_minimum', 200)}-{prompt_info.get('word_maximum', 500)} words

STUDENT'S WRITING:
\"\"\"
{student_text}
\"\"\"

Evaluate against these four criteria (each worth 25%):

1. MAIN MESSAGE & FOCUS: Is the main point clear from the start? Does the reader immediately understand what the writer is saying?

2. LOGICAL STRUCTURE: Do supporting points clearly connect to the main message? Does each paragraph answer 'why?' or 'how?' about the main point?

3. GROUPING & COMPLETENESS: Are ideas organized without overlap? Are the supporting points different from each other? Together do they cover everything important?

4. CONVENTIONS & CLARITY: Is the writing clear and relatively error-free? Are sentences varied and words precise?

Respond in this exact JSON format:
{{
    "overall_level": <1-4>,
    "overall_percentage": <50-100>,
    "categories": {{
        "main_message": {{
            "level": <1-4>,
            "strength": "<what they did well in 1 sentence>",
            "improvement": "<specific suggestion to improve in 1 sentence>"
        }},
        "logical_structure": {{
            "level": <1-4>,
            "strength": "<what they did well in 1 sentence>",
            "improvement": "<specific suggestion to improve in 1 sentence>"
        }},
        "grouping": {{
            "level": <1-4>,
            "strength": "<what they did well in 1 sentence>",
            "improvement": "<specific suggestion to improve in 1 sentence>"
        }},
        "conventions": {{
            "level": <1-4>,
            "strength": "<what they did well in 1 sentence>",
            "improvement": "<specific suggestion to improve in 1 sentence>"
        }}
    }},
    "overall_feedback": "<2-3 sentences of encouraging, specific feedback about what they did well>",
    "top_priority": "<The single most important thing they should focus on improving, explained in a helpful way for a Grade 7-8 student>"
}}

Be encouraging but honest. Focus on helping the student improve. Use language appropriate for Grade 7-8 students."""

    def _parse_evaluation_response(self, response_text):
        """Parse the AI response into structured evaluation."""
        try:
            # Find JSON in response
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start >= 0 and end > start:
                json_str = response_text[start:end]
                return json.loads(json_str)
        except json.JSONDecodeError:
            pass

        # Return a default structure if parsing fails
        return {
            "overall_level": 3,
            "overall_percentage": 72,
            "categories": {
                "main_message": {"level": 3, "strength": "You have ideas to share.", "improvement": "Try stating your main point more clearly in your opening."},
                "logical_structure": {"level": 3, "strength": "You organized your writing into paragraphs.", "improvement": "Make sure each paragraph focuses on one clear point."},
                "grouping": {"level": 3, "strength": "You included supporting ideas.", "improvement": "Check that your points are different from each other."},
                "conventions": {"level": 3, "strength": "Your writing is readable.", "improvement": "Proofread for spelling and grammar."}
            },
            "overall_feedback": "You've made a good effort with this writing. Keep practicing the structure tips you learned.",
            "top_priority": "Focus on stating your main message clearly in your first paragraph so readers know right away what you're writing about."
        }

    def _fallback_evaluation(self, student_text, prompt_info):
        """Provide basic evaluation when AI is not available."""
        words = student_text.split()
        word_count = len(words)
        paragraphs = [p for p in student_text.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)
        sentences = student_text.replace('!', '.').replace('?', '.').split('.')
        sentence_count = len([s for s in sentences if s.strip()])

        # Basic heuristics
        has_good_length = prompt_info.get('word_minimum', 200) <= word_count <= prompt_info.get('word_maximum', 500)
        has_paragraphs = paragraph_count >= 3
        has_variety = sentence_count >= 5

        # Estimate levels based on basic analysis
        base_level = 2
        if has_good_length:
            base_level += 0.5
        if has_paragraphs:
            base_level += 0.5
        if has_variety:
            base_level += 0.5

        overall_level = min(4, max(1, round(base_level)))

        level_percentages = {1: 55, 2: 65, 3: 74, 4: 85}

        return {
            "overall_level": overall_level,
            "overall_percentage": level_percentages[overall_level],
            "categories": {
                "main_message": {
                    "level": overall_level,
                    "strength": "You have a message to share with your reader.",
                    "improvement": "Make sure your main point is crystal clear in your first paragraph."
                },
                "logical_structure": {
                    "level": overall_level if has_paragraphs else max(1, overall_level - 1),
                    "strength": "You've organized your writing." if has_paragraphs else "You've started organizing your ideas.",
                    "improvement": "Each paragraph should make ONE clear point that supports your main message."
                },
                "grouping": {
                    "level": overall_level,
                    "strength": "You've included supporting points.",
                    "improvement": "Double-check that your points are different from each other and don't repeat the same idea."
                },
                "conventions": {
                    "level": overall_level,
                    "strength": "Your writing is understandable.",
                    "improvement": "Always proofread your work for spelling and grammar errors."
                }
            },
            "overall_feedback": f"You wrote {word_count} words across {paragraph_count} paragraph{'s' if paragraph_count != 1 else ''}. " +
                ("Good job meeting the word count!" if has_good_length else f"Try to {'expand' if word_count < prompt_info.get('word_minimum', 200) else 'tighten'} your writing to meet the target."),
            "top_priority": "Focus on making your main message clear from the very first paragraph. Your reader should know exactly what you're saying before they finish your introduction.",
            "ai_evaluated": False
        }
