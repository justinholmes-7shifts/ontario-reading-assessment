# Ontario Reading & Writing Assessment Tool

A web-based assessment tool for Grade 7-8 students aligned with the Ontario Language Curriculum.

## Features

- **Reading Assessments**: Comprehension tests with various passage types (fiction, non-fiction, media texts)
- **Writing Assessments**: Structured prompts with curriculum-aligned rubrics
- **Progress Tracking**: Monitor student performance across assessment areas
- **Curriculum Alignment**: Based on Ontario Language Curriculum expectations for Grades 7-8

## Ontario Curriculum Areas Covered

### Reading
- Understanding form and style
- Reading for meaning (comprehension strategies)
- Critical literacy and analysis
- Making connections (text-to-text, text-to-self, text-to-world)

### Writing
- Developing and organizing content
- Using knowledge of form and style
- Applying knowledge of conventions
- Reflecting on writing skills

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

## Project Structure

```
ontario-reading-assessment/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── assessments/       # Assessment logic
│   ├── curriculum/        # Ontario curriculum data
│   ├── templates/         # HTML templates
│   └── static/           # CSS, JS assets
├── data/
│   ├── passages/         # Reading passages
│   └── writing_prompts/  # Writing prompts
├── tests/
└── run.py
```

## Assessment Types

### Reading Assessment
- Multiple choice comprehension questions
- Short answer responses
- Inference and analysis questions
- Vocabulary in context

### Writing Assessment
- Narrative writing
- Opinion/persuasive writing
- Informational writing
- Response to text
