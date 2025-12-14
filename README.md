# Ontario Reading & Writing Assessment Tool

A Flask-based web application for Grade 7-8 reading and writing assessments, aligned with the Ontario Language Curriculum and featuring AI-powered writing feedback.

**Live Demo:** https://spartacu3131.pythonanywhere.com
**Repository:** https://github.com/justinholmes-7shifts/ontario-reading-assessment

## Current Status

**Phase:** MVP Deployed - Ready for user testing
**Last Updated:** December 13, 2024

## Features

- **Reading Assessments**: Comprehension tests with passages themed after renowned Canadian and world authors (Wagamese, Atwood, Lowry, Orwell)
- **Writing Assessments**: Genre-specific prompts (narrative, opinion, informational) with structured planning frameworks
- **AI-Powered Feedback**: Claude API integration provides formative writing feedback aligned with Ontario rubrics
- **"Think First" Framework**: Student-friendly adaptation of Pyramid Principle for critical thinking and structured communication
- **Comprehensive Guides**: Student guides for reading/writing strategies and teacher guide with detailed rubrics
- **Curriculum Alignment**: All assessments mapped to specific Ontario Language Curriculum expectations for Grades 7-8

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

### Local Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your Claude API key
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env

# Run the application
python run.py
```

Access the application at http://localhost:5000

### Production Deployment (PythonAnywhere)

Current deployment: https://spartacu3131.pythonanywhere.com

1. Upload project files to PythonAnywhere
2. Configure WSGI file to point to Flask app
3. Set ANTHROPIC_API_KEY environment variable in PythonAnywhere settings
4. Reload web app

See deployment guide in guides/ folder for detailed instructions.

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
