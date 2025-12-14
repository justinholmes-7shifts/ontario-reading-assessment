# Ontario Reading Assessment - AI Context File

**Last Updated:** December 13, 2024
**Project Phase:** MVP Deployed - Ready for User Testing

---

## Project Overview

Flask-based web application for Ontario Grade 7-8 reading and writing assessments with AI-powered feedback.

**Live Application:** https://spartacu3131.pythonanywhere.com
**Repository:** https://github.com/justinholmes-7shifts/ontario-reading-assessment

**Core Innovation:** Embedding business communication best practices (Pyramid Principle) within grade-appropriate assessment tools under student-friendly "Think First" framework.

---

## Project State

### Current Workflow Phase

**Workflow Stages:**
- [x] Idea & Validation
- [x] Research & Planning
- [x] Core Development
- [x] Initial Deployment
- [ ] User Testing
- [ ] Iteration Based on Feedback
- [ ] Production Launch
- [ ] Maintenance & Enhancement

**Current Phase:** User Testing Preparation

**Completed in This Session:**
- [x] Flask application structure
- [x] Reading assessment with themed passages
- [x] Writing assessment with AI evaluation
- [x] Student guides (reading and writing)
- [x] Teacher assessment guide with rubrics
- [x] GitHub repository setup
- [x] PythonAnywhere deployment
- [x] WSGI configuration
- [x] Environment variable setup

**Next Steps:**
- [ ] End-to-end testing of deployed application
- [ ] Mobile responsiveness verification
- [ ] Error handling for API failures
- [ ] Content expansion (more passages and prompts)
- [ ] Teacher user testing
- [ ] Student usability testing

---

## Key Decisions & Context

### Idea & Validation

**Core Idea:**
Create a web-based assessment tool that serves dual purposes:
1. Meet Ontario Grade 7-8 Language Curriculum requirements
2. Secretly teach Pyramid Principle structured thinking

**Target Audience:**
- Primary: Grade 7-8 students in Ontario schools
- Secondary: Teachers administering language assessments
- Context: Students aged 12-14, diverse reading levels, varying tech access

**Validation Approach:**
- Align with published Ontario Language Curriculum expectations
- Reference standardized assessment formats (EQAO-style)
- Incorporate pedagogy from educational literature
- Test with teachers before broader rollout

### Research Insights

**Ontario Curriculum Requirements:**
- Reading: Comprehension strategies, critical literacy, making connections, form and style analysis
- Writing: Content development, organization, form/style knowledge, conventions, reflection
- Assessment: 4-point rubric scale (Limited, Some, Considerable, High Degree)

**Technical Findings:**
- PythonAnywhere supports Flask apps with simple WSGI configuration
- Claude API provides curriculum-aligned writing feedback
- No database needed for MVP (session-based storage sufficient)

**Educational Best Practices:**
- Formative feedback more valuable than summative scores alone
- Metacognitive strategies improve comprehension
- Rubric transparency supports student self-assessment
- Cultural relevance increases engagement

### Creative Strategy

**Pedagogical Angle:**
"Think First" framework as accessible entry point to structured thinking:
- Students learn to identify main ideas (pyramid top)
- Practice organizing supporting details (MECE grouping)
- Build evidence-based arguments (supporting layers)
- Develop clear communication structure (top-down presentation)

**Content Hooks:**
- Passages themed after recognizable authors (Wagamese, Atwood, Lowry, Orwell)
- Culturally diverse representation (Indigenous perspectives, Canadian settings)
- Age-appropriate complexity with engaging topics

**Assessment Structure:**
- Reading: 4 passages, mixed question types (multiple choice, short answer, inference)
- Writing: Genre-specific prompts with planning frameworks
- AI feedback: Constructive, specific, encouraging tone

### Production Decisions

**Technology Stack:**
- Backend: Flask 3.0+ (simplicity, lightweight, easy deployment)
- AI: Anthropic Claude API (high-quality feedback generation)
- Deployment: PythonAnywhere (no infrastructure management, teacher-accessible)
- Version Control: Git + GitHub (open source, community contributions)

**Architecture Choices:**
- Modular assessment structure (`/app/assessments/` for each type)
- Separation of curriculum data (`/app/curriculum/`)
- No database for MVP (reduces complexity, privacy concerns)
- Environment variables for API keys (security best practice)

**Design Principles:**
- Progressive enhancement (works without JavaScript)
- Mobile-responsive (students may use tablets/phones)
- Privacy-first (no student data collection/storage)
- Open source (educators can adapt and extend)

---

## Working Instructions

### Current Focus

**Primary Goal:** Validate deployment and prepare for user testing

**Success Criteria:**
1. Application runs smoothly on PythonAnywhere
2. Claude API integration works reliably
3. All guides are accessible and helpful
4. Teachers can understand rubrics and administer assessments
5. Students can navigate interface independently

### Code Modification Guidelines

**When Editing Python Code:**
- Maintain Flask blueprint pattern if adding new modules
- All assessment logic goes in `/app/assessments/`
- Use environment variables for all configuration
- Add docstrings to functions (explain Ontario curriculum alignment)
- Keep functions focused and testable

**When Creating Content:**
- Reading passages: 400-600 words, grade 7-8 reading level
- Writing prompts: Clear task, defined audience, specific purpose
- All content must map to specific Ontario curriculum expectations
- Include diverse cultural perspectives and Canadian references

**When Updating Guides:**
- Student-facing: Encouraging tone, jargon-free, examples included
- Teacher-facing: Detailed rubrics, curriculum codes, differentiation strategies
- Keep consistent formatting with existing guides

### Relevant Workflows

**Adding New Reading Passage:**
1. Create passage file in `/data/passages/`
2. Develop 6-8 questions (mix multiple choice, short answer, inference)
3. Map questions to curriculum expectations
4. Add answer key and rubric notes to teacher guide
5. Test readability (Flesch-Kincaid grade level)

**Adding New Writing Prompt:**
1. Create prompt in `/data/writing_prompts/`
2. Specify genre (narrative, opinion, informational)
3. Define task, audience, purpose clearly
4. Create sample "Think First" organizer
5. Add rubric guidance to teacher guide
6. Test AI feedback generation with sample responses

**Updating AI Evaluator:**
1. Modify prompts in `/app/assessments/ai_evaluator.py`
2. Ensure alignment with Ontario rubric language
3. Test with varied student writing samples
4. Verify constructive, grade-appropriate tone
5. Handle API errors gracefully (fallback messaging)

**Deployment Updates:**
1. Test locally first (`python run.py`)
2. Commit changes to Git
3. Push to GitHub
4. Upload modified files to PythonAnywhere
5. Reload web app via PythonAnywhere dashboard
6. Test live deployment

---

## Technical Architecture

### File Structure
```
ontario-reading-assessment/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── routes.py                # URL routing
│   ├── assessments/
│   │   ├── __init__.py
│   │   ├── reading.py           # Reading assessment logic
│   │   ├── writing.py           # Writing assessment logic
│   │   └── ai_evaluator.py      # Claude API integration
│   ├── curriculum/
│   │   └── __init__.py          # Ontario curriculum data
│   ├── templates/               # HTML templates
│   └── static/                  # CSS, JS, images
├── data/
│   ├── passages/                # Reading passages
│   └── writing_prompts/         # Writing prompts
├── guides/
│   ├── STUDENT_GUIDE_READING.md
│   ├── STUDENT_GUIDE_WRITING.md
│   └── TEACHER_ASSESSMENT_GUIDE.md
├── tests/                       # Unit tests (future)
├── .env                         # Environment variables (not in Git)
├── .gitignore
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
└── README.md
```

### Key Dependencies
- **flask**: Web framework
- **python-dotenv**: Environment variable management
- **anthropic**: Claude API client

### Environment Variables
- `ANTHROPIC_API_KEY`: Required for AI writing feedback
- `FLASK_ENV`: development/production (optional)
- `SECRET_KEY`: Flask session security (future if adding auth)

---

## Content Guidelines

### Reading Passages
**Themes Developed:**
- Richard Wagamese-inspired: Indigenous connection to land, intergenerational wisdom
- Margaret Atwood-inspired: Canadian dystopian fiction, social commentary
- Lois Lowry-inspired: Coming-of-age moral complexity, difficult choices
- George Orwell-inspired: Surveillance, social control, resistance

**Future Passage Ideas:**
- Science/nature writing (David Suzuki style)
- Historical fiction (Canadian history themes)
- Poetry analysis
- Media texts (advertisements, articles)

### Writing Prompts
**Current Coverage:**
- Narrative: Personal experience, fictional story
- Opinion: Persuasive argument on relevant topic
- Informational: Explanatory text on curriculum theme

**Future Prompt Ideas:**
- Response to text (connect to reading passages)
- Procedural writing (how-to instructions)
- Comparative analysis (two texts/perspectives)

### "Think First" Framework
**Core Components:**
1. **What's the big picture?** (Main idea/thesis)
2. **How do I organize my thoughts?** (MECE grouping)
3. **What evidence supports this?** (Details, examples, quotes)
4. **How do I communicate clearly?** (Top-down structure)

**Application in Reading:**
- Identify main idea before details
- Group information into categories
- Find text evidence for inferences
- Summarize top-down (main point first)

**Application in Writing:**
- Start with clear thesis/main point
- Organize supporting ideas in logical groups
- Use specific evidence for each point
- Structure paragraphs top-down (topic sentence first)

---

## Open Questions & Future Considerations

### Technical
- Should we add database for progress tracking across sessions?
- How to handle multiple teachers using same instance (multi-tenancy)?
- Offline mode for writing assessments (no internet required)?
- API rate limiting and cost management for Claude API?

### Pedagogical
- How often should students use this tool? (Diagnostic, formative, summative?)
- Should AI feedback be visible to students immediately or after teacher review?
- How to validate AI feedback quality matches teacher judgment?
- Student choice in writing prompts vs. assigned prompts?

### Content
- How many reading passages needed for full assessment bank?
- Should we include accommodations (text-to-speech, extended time)?
- Translations for ESL students?
- Differentiated versions of passages (same theme, varied complexity)?

### Deployment & Scaling
- How to support multiple school instances (each with own data)?
- Privacy-compliant usage analytics to improve tool?
- Process for teachers to submit new content (passages, prompts)?
- Commercial vs. open-source model?

---

## User Testing Plan

### Teacher Testing
**Participants:** 2-3 Ontario elementary/middle school teachers
**Focus Areas:**
- Curriculum alignment validation
- Rubric clarity and usability
- Assessment administration workflow
- AI feedback quality and appropriateness
- Time requirements

**Questions:**
1. Are rubrics clear and aligned with your grading practices?
2. Is the teacher guide sufficient for administering assessments?
3. Does AI feedback match your assessment of student writing?
4. What additional content (passages/prompts) would you need?
5. What barriers to adoption do you see?

### Student Testing
**Participants:** 1-2 students (Grade 7-8, if possible)
**Focus Areas:**
- Interface usability
- Instruction clarity
- Question comprehension
- "Think First" framework usefulness
- Engagement level

**Questions:**
1. Were the instructions clear?
2. Did you understand what each question was asking?
3. Was the "Think First" framework helpful for planning?
4. Was the AI feedback helpful and encouraging?
5. What was confusing or frustrating?

### Testing Protocol
1. Brief demo of tool (5 minutes)
2. Observed use (15-20 minutes)
3. Think-aloud protocol (ask users to verbalize thoughts)
4. Post-use interview (10 minutes)
5. Written feedback form

---

## Success Metrics

### MVP Success Criteria
- [ ] Application loads without errors on PythonAnywhere
- [ ] All reading passages display correctly
- [ ] Writing prompts load and accept text input
- [ ] Claude API returns feedback within 10 seconds
- [ ] Mobile-responsive on tablets and phones
- [ ] Teacher guide rubrics are understandable to educators
- [ ] Student guides are readable at grade 7-8 level

### User Testing Success Criteria
- [ ] 80%+ of teachers agree rubrics are curriculum-aligned
- [ ] 80%+ of teachers find AI feedback appropriate and helpful
- [ ] Students can complete assessment independently (minimal teacher intervention)
- [ ] Students report "Think First" framework is useful
- [ ] No major technical errors during testing

### Long-term Success Criteria (Future)
- Adoption by 10+ Ontario teachers
- Positive impact on student writing quality (validated by teachers)
- Content bank of 20+ passages and 30+ prompts
- Community contributions (teachers submitting content)
- Research partnership to validate effectiveness

---

## Maintenance & Support

### Regular Maintenance Tasks
- Monitor Claude API usage and costs
- Review and update reading passages for currency
- Ensure Ontario curriculum alignment as curriculum evolves
- Update dependencies (Flask, Anthropic SDK)
- Address user-reported issues

### Support Resources
- GitHub Issues for bug reports and feature requests
- Teacher guide includes troubleshooting section
- Email support (to be determined)
- Community forum (future consideration)

---

## Contributing Guidelines (Future)

### Content Contributions
Teachers can submit:
- New reading passages (with curriculum mapping)
- Writing prompts (with rubric guidance)
- Assessment questions
- "Think First" framework adaptations

**Submission Process:**
1. Fork repository on GitHub
2. Add content following existing format
3. Include curriculum expectation codes
4. Submit pull request with rationale

### Code Contributions
Developers can contribute:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Accessibility improvements

**Development Standards:**
- Follow PEP 8 Python style guide
- Include docstrings with curriculum context
- Write unit tests for new features
- Update README with new functionality

---

## Contact & Attribution

**Project Creator:** Justin Holmes
**GitHub:** https://github.com/justinholmes-7shifts
**License:** To be determined (consider open-source education license)

**Acknowledgments:**
- Ontario Ministry of Education (curriculum framework)
- Anthropic (Claude API)
- Flask community
- PythonAnywhere

---

## Quick Reference Commands

### Local Development
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python run.py

# Deactivate virtual environment
deactivate
```

### Git Workflow
```bash
# Check status
git status

# Add changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

### PythonAnywhere Deployment
1. Upload files via web interface or Git pull
2. Navigate to Web tab
3. Edit WSGI configuration file
4. Set environment variables in "Environment variables" section
5. Click "Reload" button
6. Check error logs if issues occur

---

## Notes for AI Assistants

**Context Preservation:**
When helping with this project, maintain awareness of:
- Dual purpose (assessment + structured thinking instruction)
- Ontario curriculum compliance is non-negotiable
- Age-appropriate language for 12-14 year olds
- Privacy-first approach (no student data collection)
- Teacher authority over AI feedback (AI suggests, teachers decide)

**Code Style:**
- Clear, documented Python code
- Flask best practices
- Security-conscious (environment variables, input validation)
- Accessible HTML (semantic markup, ARIA labels)

**Content Style:**
- Student guides: Encouraging, clear, example-rich
- Teacher guides: Detailed, professional, curriculum-referenced
- Assessment content: Engaging, diverse, grade-appropriate

**Future AI Integration:**
Consider opportunities to enhance (but maintain core privacy/pedagogy principles):
- Personalized feedback based on student patterns
- Adaptive difficulty (while maintaining fair assessment)
- Teacher analytics (aggregated, privacy-compliant)
- Accessibility features (text-to-speech, translation)
