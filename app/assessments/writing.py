"""
Writing Assessment Module
Aligned with Ontario Language Curriculum Grade 7-8

Embeds structured thinking principles to develop logical communication skills.
"""

from app.curriculum import WRITING_EXPECTATIONS, WRITING_RUBRIC, ACHIEVEMENT_LEVELS
from app.assessments.ai_evaluator import AIEvaluator


# Think First Framework - guides students through structured planning
THINK_FIRST_FRAMEWORK = {
    "step_1": {
        "name": "Understand the Situation",
        "prompt": "What's happening? What background does your reader need to know?",
        "description": "Set the scene so your reader understands the context."
    },
    "step_2": {
        "name": "Identify the Challenge",
        "prompt": "What's the problem, tension, or interesting question here?",
        "description": "What makes this worth writing about? What needs to be resolved or explained?"
    },
    "step_3": {
        "name": "Focus Your Message",
        "prompt": "If you could only tell your reader ONE thing, what would it be?",
        "description": "This is your main point. Everything else should support this."
    },
    "step_4": {
        "name": "Build Your Support",
        "prompt": "What are 2-4 different reasons or points that support your main message?",
        "description": "Group similar ideas together. Make sure each point is different and together they cover everything important."
    },
    "step_5": {
        "name": "Check Your Logic",
        "prompt": "Does each supporting point answer 'why?' or 'how?' about your main message?",
        "description": "Your reader should be able to follow your thinking step by step."
    }
}


class WritingAssessment:
    """Handles writing assessments with curriculum-aligned rubrics and structured thinking."""

    def __init__(self):
        self.prompts = self._load_prompts()
        self.rubric = WRITING_RUBRIC
        self.think_first = THINK_FIRST_FRAMEWORK
        self.ai_evaluator = AIEvaluator()

    def _load_prompts(self):
        """Load writing prompts aligned with Ontario curriculum and structured thinking."""
        return {
            "narrative_1": {
                "id": "narrative_1",
                "title": "A Moment That Changed Everything",
                "grade": "7-8",
                "type": "Narrative Writing",
                "prompt": """
Write a narrative about a moment when you (or a character) faced a difficult decision
that changed everything.

**Start with the moment of change** - hook your reader by showing why this moment matters.
Then build the story around it.

Your story should include:
- An opening that shows the reader why this moment is important
- The situation: who, where, when, and what was happening
- The challenge: what made the decision so difficult
- The choice: what happened and why
- The change: how things were different after

Your narrative should be 3-5 paragraphs in length.
                """,
                "think_first_guide": {
                    "situation": "Who is your character? What was life like before the big moment?",
                    "challenge": "What difficult decision did they face? What made it hard?",
                    "focus": "What's the ONE big change or lesson from this story?",
                    "support": [
                        "What events led to the decision?",
                        "What did the character think and feel?",
                        "What happened because of their choice?"
                    ],
                    "logic_check": "Does each part of your story connect to the main change?"
                },
                "planning_questions": [
                    "What is the ONE big change or lesson in your story? (Write this first!)",
                    "What situation led to the difficult decision?",
                    "What made this decision so hard? (the challenge)",
                    "What 2-3 key events show how your character changed?",
                    "Do your events connect logically - does each one lead to the next?"
                ],
                "structure_tips": [
                    "Start with the moment that matters most - hook your reader immediately",
                    "Every scene should connect to your main message about change",
                    "Group related events together in the same paragraph",
                    "Make sure your events don't repeat the same idea - each should add something new"
                ],
                "success_criteria": [
                    "Opens with a clear hook that shows why this story matters",
                    "Each paragraph has ONE clear purpose that supports the main message",
                    "Events are grouped logically and don't overlap",
                    "The reader can follow your thinking from beginning to end",
                    "Vivid details that help readers visualize the story",
                    "Resolution clearly connects back to your opening",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 250,
                "word_maximum": 500
            },
            "persuasive_1": {
                "id": "persuasive_1",
                "title": "Screen Time: Help or Harm?",
                "grade": "7-8",
                "type": "Opinion/Persuasive Writing",
                "prompt": """
Many adults worry that teenagers spend too much time on screens. Others argue that
screen time can be educational and beneficial.

**Lead with your answer.** State your position clearly in your first paragraph, then
prove why you're right.

Your essay should include:
- Your main argument stated clearly upfront (don't make readers guess!)
- 2-3 different reasons that each support your position
- Evidence or examples for each reason (each reason answers "why?" about your main point)
- Brief acknowledgment of the other side (and why your view is still stronger)
- A conclusion that reinforces your main message

Your essay should be 4-5 paragraphs in length.
                """,
                "think_first_guide": {
                    "situation": "What's the debate about screen time? Why does it matter?",
                    "challenge": "Why do people disagree? What makes this complicated?",
                    "focus": "What's YOUR answer? (State this clearly - this is your thesis!)",
                    "support": [
                        "Reason 1: Why is your position correct? (First strongest point)",
                        "Reason 2: What's another different reason? (Don't repeat!)",
                        "Reason 3: What else supports your view? (Covers new ground)"
                    ],
                    "logic_check": "Does each reason answer 'why?' about your main position? Are they different from each other?"
                },
                "planning_questions": [
                    "What is your MAIN ARGUMENT in one sentence? (Write this first!)",
                    "What's happening with screen time that makes people concerned?",
                    "What's the challenge - why do people disagree about this?",
                    "List 2-3 DIFFERENT reasons supporting your position (no overlapping!)",
                    "For each reason: does it directly answer 'why?' about your main argument?",
                    "What would someone who disagrees say? Why is your view still stronger?"
                ],
                "structure_tips": [
                    "Put your main argument in the first paragraph - don't make readers wait",
                    "Each body paragraph = ONE reason (don't mix multiple reasons together)",
                    "Your reasons should be different from each other, not variations of the same idea",
                    "Together, your reasons should cover the most important points (nothing major missing)",
                    "End by circling back to your main argument"
                ],
                "success_criteria": [
                    "Main argument is stated clearly in the introduction",
                    "Each body paragraph focuses on ONE distinct supporting reason",
                    "Reasons don't overlap - each adds something new",
                    "Evidence directly supports each reason",
                    "Reader can follow the logic: main point → reason → evidence",
                    "Counterargument is addressed",
                    "Conclusion reinforces the main argument",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 300,
                "word_maximum": 600
            },
            "informational_1": {
                "id": "informational_1",
                "title": "Explaining a Process",
                "grade": "7-8",
                "type": "Informational/Explanatory Writing",
                "prompt": """
Think of something you know how to do well—it could be a hobby, a skill, a game,
or any process you can explain clearly.

**Start with the big picture.** Tell readers what they'll learn and why it matters
before diving into details.

Your essay should include:
- An opening that explains what this process achieves and why it's useful
- Steps grouped into logical stages (not just a long list!)
- Each stage should answer "how?" about achieving the goal
- Specific details within each stage
- A conclusion that reminds readers of the main outcome

Your essay should be 4-5 paragraphs in length.
                """,
                "think_first_guide": {
                    "situation": "What process will you explain? Who would want to learn this?",
                    "challenge": "What makes this tricky to learn? What do beginners struggle with?",
                    "focus": "What's the END RESULT readers will achieve? (State this upfront!)",
                    "support": [
                        "Stage 1: What's the first major phase? (Group related steps)",
                        "Stage 2: What comes next? (A different phase, not just more steps)",
                        "Stage 3: How do you finish? (Final phase to reach the goal)"
                    ],
                    "logic_check": "Does each stage answer 'how?' about reaching the goal? Are stages clearly different?"
                },
                "planning_questions": [
                    "What will readers be able to DO after reading this? (State the goal first!)",
                    "What situation are your readers in? Why would they want to learn this?",
                    "What's challenging about this process?",
                    "What are 2-4 major STAGES (not individual steps - group related steps together)?",
                    "Does each stage directly help achieve the goal? (answers 'how?')",
                    "Are your stages different from each other and in logical order?"
                ],
                "structure_tips": [
                    "Start with the outcome - tell readers what they'll achieve",
                    "Group small steps into bigger stages (don't list 15 tiny steps)",
                    "Each paragraph = one stage (related steps grouped together)",
                    "Stages should be different categories, not just 'more steps'",
                    "Order matters: each stage builds on the previous one"
                ],
                "success_criteria": [
                    "Opening clearly states what readers will learn and why it matters",
                    "Steps are grouped into logical stages (not just listed)",
                    "Each stage is distinct and answers 'how?' about the goal",
                    "Stages are in logical order - each builds on the last",
                    "Specific helpful details within each stage",
                    "Conclusion reminds readers of the outcome",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 250,
                "word_maximum": 500
            },
            "response_1": {
                "id": "response_1",
                "title": "Response to Text",
                "grade": "7-8",
                "type": "Response to Reading",
                "prompt": """
Think about a book, article, movie, or other text that made you think deeply about
an important issue or changed your perspective.

**Lead with your insight.** Start with the main idea you want to share, then explain
how the text led you to that thinking.

Your response should:
- Open with your key insight or takeaway (don't bury it at the end!)
- Identify the text and the relevant theme or idea
- Share 2-3 different ways this text affected your thinking
- Use specific evidence from the text to support your points
- Connect back to why this insight matters

Your response should be 3-4 paragraphs in length.
                """,
                "think_first_guide": {
                    "situation": "What text are you responding to? What's it about?",
                    "challenge": "What issue or question does this text raise?",
                    "focus": "What's your MAIN INSIGHT from this text? (Lead with this!)",
                    "support": [
                        "Point 1: One way the text affected your thinking",
                        "Point 2: A different way it affected you (not the same idea)",
                        "Point 3: Another distinct connection or impact"
                    ],
                    "logic_check": "Does each point connect to your main insight? Are they different from each other?"
                },
                "planning_questions": [
                    "What is your MAIN INSIGHT from this text? (Write this first!)",
                    "What text are you discussing and what is it about?",
                    "What question or issue does this text make you think about?",
                    "List 2-3 DIFFERENT ways this text affected your thinking",
                    "For each point: what specific evidence from the text supports it?",
                    "Do your points overlap, or is each one distinct?"
                ],
                "structure_tips": [
                    "Start with your main insight - this is your answer, not your conclusion",
                    "Each body point should be a different aspect of how the text affected you",
                    "Don't just summarize the text - analyze how it changed your thinking",
                    "Your points should work together to fully explain your insight",
                    "End by showing why this insight matters beyond just this text"
                ],
                "success_criteria": [
                    "Opens with a clear statement of your main insight",
                    "Text is identified with relevant context",
                    "Each supporting point is distinct (no overlap)",
                    "Points together fully explain your insight",
                    "Specific textual evidence supports each point",
                    "Conclusion connects back to the significance of your insight",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 200,
                "word_maximum": 400
            },
            "problem_solving_1": {
                "id": "problem_solving_1",
                "title": "Solving a School Problem",
                "grade": "7-8",
                "type": "Problem-Solution Writing",
                "prompt": """
Think about a problem at your school that you think should be fixed (examples:
cafeteria issues, homework policies, schedule problems, social issues, etc.)

**Structure your thinking:** Clearly explain the situation, identify what makes it
a problem, and propose a solution with reasons why it would work.

Your essay should include:
- The situation: What's happening at your school?
- The problem: Why is this situation a problem? Who is affected and how?
- Your solution: What should be done? (State this clearly!)
- Your reasoning: 2-3 different reasons why your solution would work
- Conclusion: What would improve if your solution was adopted?

Your essay should be 4-5 paragraphs in length.
                """,
                "think_first_guide": {
                    "situation": "What's happening at your school? Give context.",
                    "challenge": "Why is this a PROBLEM? What negative effects does it cause?",
                    "focus": "What's your SOLUTION? (State this clearly after explaining the problem)",
                    "support": [
                        "Reason 1: Why would this solution work? (Strongest point first)",
                        "Reason 2: What's another benefit? (Different from Reason 1)",
                        "Reason 3: What else supports this solution?"
                    ],
                    "logic_check": "Does each reason answer 'why would this work?' Are reasons distinct?"
                },
                "planning_questions": [
                    "What SITUATION exists at your school? (Background)",
                    "What makes this a PROBLEM? What's wrong with this situation?",
                    "What is your SOLUTION in one clear sentence?",
                    "List 2-3 DIFFERENT reasons why your solution would work",
                    "Does each reason directly support why your solution is good?",
                    "Are your reasons different from each other (no overlap)?",
                    "Together, do your reasons cover the most important benefits?"
                ],
                "structure_tips": [
                    "Follow this order: Situation → Problem → Solution → Reasons",
                    "The problem should make readers understand WHY change is needed",
                    "State your solution clearly before explaining why it works",
                    "Each reason should be a different type of benefit (don't repeat)",
                    "Your reasons together should convince readers your solution is complete"
                ],
                "success_criteria": [
                    "Situation is clearly explained with enough context",
                    "Problem is defined: why the situation is bad and who it affects",
                    "Solution is stated clearly and specifically",
                    "Each reason is distinct and supports the solution",
                    "Reasons together make a complete argument",
                    "Conclusion shows the positive outcome of the solution",
                    "Correct spelling, grammar, and punctuation"
                ],
                "curriculum_alignment": ["developing_ideas", "form_and_style", "conventions"],
                "word_minimum": 300,
                "word_maximum": 550
            }
        }

    def get_available_prompts(self):
        """Return list of available writing prompts."""
        return [
            {
                "id": p["id"],
                "title": p["title"],
                "type": p["type"],
                "grade": p["grade"],
                "word_minimum": p["word_minimum"],
                "word_maximum": p["word_maximum"]
            }
            for p in self.prompts.values()
        ]

    def get_prompt(self, prompt_id):
        """Get a specific prompt by ID."""
        prompt = self.prompts.get(prompt_id)
        if prompt:
            # Add the Think First framework to the prompt
            prompt["think_first_framework"] = self.think_first
        return prompt

    def evaluate_writing(self, prompt_id, response_text):
        """
        Evaluate student writing using AI assessment.

        Args:
            prompt_id: ID of the writing prompt
            response_text: Student's written response

        Returns:
            Assessment with scores, feedback, and improvement suggestions
        """
        prompt = self.prompts.get(prompt_id)
        if not prompt:
            return {"error": "Prompt not found"}

        # Basic text analysis
        words = response_text.split()
        word_count = len(words)
        sentences = response_text.replace('!', '.').replace('?', '.').split('.')
        sentence_count = len([s for s in sentences if s.strip()])
        paragraphs = response_text.split('\n\n')
        paragraph_count = len([p for p in paragraphs if p.strip()])

        # Get AI evaluation
        prompt_info = {
            "title": prompt["title"],
            "type": prompt["type"],
            "word_minimum": prompt["word_minimum"],
            "word_maximum": prompt["word_maximum"]
        }
        ai_evaluation = self.ai_evaluator.evaluate_writing(response_text, prompt_info)

        # Build results
        results = {
            "prompt_id": prompt_id,
            "prompt_title": prompt["title"],
            "prompt_type": prompt["type"],
            "text_metrics": {
                "word_count": word_count,
                "sentence_count": sentence_count,
                "paragraph_count": paragraph_count,
                "word_minimum": prompt["word_minimum"],
                "word_maximum": prompt["word_maximum"]
            },
            "evaluation": ai_evaluation,
            "ai_powered": self.ai_evaluator.is_available()
        }

        return results

    def _get_rubric_for_type(self, prompt_type):
        """Get assessment rubric with structured thinking criteria."""
        return {
            "categories": [
                {
                    "name": "Main Message & Focus",
                    "weight": "25%",
                    "description": "Is the main point clear from the start?",
                    "levels": {
                        "Level 4 (80-100%)": "Main message is crystal clear from the opening; reader immediately understands the point",
                        "Level 3 (70-79%)": "Main message is clear and stated early in the writing",
                        "Level 2 (60-69%)": "Main message is present but may be buried or unclear",
                        "Level 1 (50-59%)": "Main message is missing or very difficult to identify"
                    }
                },
                {
                    "name": "Logical Structure",
                    "weight": "25%",
                    "description": "Do supporting points clearly connect to the main message?",
                    "levels": {
                        "Level 4 (80-100%)": "Each paragraph directly answers 'why?' or 'how?' about the main message; points are distinct and complete",
                        "Level 3 (70-79%)": "Supporting points connect to main message with clear logic",
                        "Level 2 (60-69%)": "Some connection between points and main message, but logic may be unclear",
                        "Level 1 (50-59%)": "Points seem disconnected or don't clearly support the main message"
                    }
                },
                {
                    "name": "Grouping & Completeness",
                    "weight": "25%",
                    "description": "Are ideas grouped well? Do they cover everything important without repeating?",
                    "levels": {
                        "Level 4 (80-100%)": "Ideas are perfectly grouped; no overlap between points; nothing important is missing",
                        "Level 3 (70-79%)": "Ideas are well-grouped with minimal overlap; covers main points",
                        "Level 2 (60-69%)": "Some grouping attempted but ideas may overlap or important points may be missing",
                        "Level 1 (50-59%)": "Ideas are jumbled, repetitive, or major points are missing"
                    }
                },
                {
                    "name": "Conventions & Clarity",
                    "weight": "25%",
                    "description": "Is the writing clear and error-free?",
                    "levels": {
                        "Level 4 (80-100%)": "Virtually no errors; writing is exceptionally clear",
                        "Level 3 (70-79%)": "Few errors that don't impede understanding",
                        "Level 2 (60-69%)": "Some errors that may impede understanding",
                        "Level 1 (50-59%)": "Frequent errors that significantly impede understanding"
                    }
                }
            ]
        }

    def _get_structure_check_questions(self):
        """Questions to help students check their logical structure."""
        return [
            "Can you state your main message in ONE sentence? Is that sentence in your opening?",
            "For each paragraph: what ONE point does it make? Write it in the margin.",
            "Do your paragraph points answer 'why?' or 'how?' about your main message?",
            "Look at your paragraph points: are they all different, or do some repeat the same idea?",
            "Together, do your points cover everything important? Is anything major missing?",
            "Can a reader follow your logic from start to finish without getting confused?"
        ]

    def _get_self_assessment_questions(self, prompt_type):
        """Get self-assessment questions based on writing type."""
        # Universal structure questions
        base_questions = [
            "Is my main message/point clear in the first paragraph?",
            "Does each paragraph have ONE clear purpose?",
            "Does each paragraph support my main message?",
            "Are my supporting points different from each other (no repeating)?",
            "Together, do my points cover everything important?",
            "Can readers follow my logic from beginning to end?",
            "Did I proofread for spelling and grammar errors?"
        ]

        type_specific = {
            "Narrative Writing": [
                "Does my opening hook show why this story matters?",
                "Does every scene connect to the main change/lesson?",
                "Are my events in an order that makes sense?",
                "Does my ending connect back to my opening?"
            ],
            "Opinion/Persuasive Writing": [
                "Is my position stated clearly in the first paragraph?",
                "Is each reason a DIFFERENT type of argument?",
                "Does each reason directly answer 'why is my position correct?'",
                "Did I address the other side of the argument?"
            ],
            "Informational/Explanatory Writing": [
                "Did I start with what readers will achieve?",
                "Are my steps grouped into logical stages (not just listed)?",
                "Does each stage answer 'how?' about reaching the goal?",
                "Are my stages in an order that builds logically?"
            ],
            "Response to Reading": [
                "Did I lead with my main insight (not bury it)?",
                "Is each point a different way the text affected me?",
                "Do my points together explain my full insight?",
                "Did I use specific evidence from the text?"
            ],
            "Problem-Solution Writing": [
                "Did I clearly explain the situation before the problem?",
                "Is it clear WHY this situation is a problem?",
                "Is my solution stated clearly before my reasons?",
                "Does each reason answer 'why would this solution work?'"
            ]
        }

        return base_questions + type_specific.get(prompt_type, [])

    def get_think_first_framework(self):
        """Return the Think First planning framework."""
        return self.think_first
