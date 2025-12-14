# Ontario Reading Assessment - Next Session TODO

**Created:** December 13, 2024
**Session Focus:** Post-Deployment Testing & Content Expansion

---

## Immediate Next Steps

### Testing & Validation
- [ ] **Test live PythonAnywhere deployment end-to-end**
  - Visit https://spartacu3131.pythonanywhere.com
  - Complete full reading assessment (all question types)
  - Complete writing assessment (submit text, verify AI feedback)
  - Test on desktop, tablet, and mobile devices
  - Document any errors or unexpected behavior

- [ ] **Verify Claude API integration**
  - Confirm ANTHROPIC_API_KEY environment variable is set correctly
  - Test writing feedback generation (submit sample student writing)
  - Check API response time (should be <10 seconds)
  - Review feedback quality (constructive, curriculum-aligned, grade-appropriate)

- [ ] **Test error handling**
  - What happens if Claude API is down or times out?
  - How does app handle missing environment variables?
  - Are error messages user-friendly for students/teachers?

- [ ] **Accessibility check**
  - Test with screen reader (basic accessibility)
  - Verify keyboard navigation works
  - Check color contrast for readability
  - Ensure form labels are properly associated

### Content Expansion
- [ ] **Create additional reading passages** (target: 3-4 more passages)
  - Science/nature writing theme (David Suzuki style)
  - Canadian historical fiction
  - Media text (article or advertisement analysis)
  - Poetry passage

- [ ] **Expand writing prompt bank** (target: 10 prompts per genre)
  - 10 narrative prompts (currently have ~2)
  - 10 opinion/persuasive prompts
  - 10 informational prompts
  - Add "response to text" prompts connected to reading passages

- [ ] **Create sample scored responses**
  - Write example responses at each rubric level (Limited, Some, Considerable, High)
  - Add to teacher guide for calibration
  - Use for AI feedback validation

### Documentation
- [ ] **Create deployment guide for educators**
  - Step-by-step PythonAnywhere setup instructions
  - How to obtain Claude API key
  - Environment variable configuration
  - Troubleshooting common issues

- [ ] **Write contributing guidelines**
  - How teachers can submit passages/prompts
  - Content format requirements
  - Curriculum mapping standards
  - Pull request process

- [ ] **Document API usage and costs**
  - Estimate tokens per writing assessment
  - Calculate monthly cost projections
  - Budget planning guidance for schools
  - Alternative solutions if API costs are barrier

---

## Questions to Answer

### Technical Questions
1. **Data persistence:** Do we need to add database for student progress tracking across sessions, or is session-based storage sufficient?
2. **Multi-tenancy:** If multiple teachers want to use this, how do we isolate their data? Separate PythonAnywhere instances?
3. **API key management:** Should each teacher use their own Claude API key, or can we safely share one?
4. **Offline functionality:** Should writing assessments work without internet (no AI feedback), or always require connection?

### Pedagogical Questions
1. **Assessment frequency:** Should this be used for diagnostic (beginning of year), formative (ongoing), or summative (final) assessment?
2. **AI feedback timing:** Should students see AI feedback immediately, or only after teacher review?
3. **AI feedback validation:** How do we verify AI feedback quality aligns with teacher professional judgment?
4. **Student agency:** Should students choose their own writing prompts from a bank, or should teachers assign specific ones?
5. **Accommodations:** What modifications needed for students with IEPs (text-to-speech, extended time, simplified language)?

### Content Questions
1. **Passage variety:** What's the minimum number of passages needed for a robust assessment bank that prevents memorization?
2. **Cultural representation:** Are we including sufficient diversity in authors, themes, and perspectives?
3. **Curriculum updates:** Ontario curriculum is under review - how do we stay aligned with changes?
4. **Differentiation:** Should we create multiple versions of same passage at different reading levels?

### Deployment Questions
1. **Scaling:** If 10+ schools want to use this, what's the deployment model? (Individual instances, shared platform, etc.)
2. **Privacy compliance:** Do we need privacy policy, terms of service, parental consent forms?
3. **Usage analytics:** What metrics would help improve the tool while respecting student privacy?
4. **Support model:** Who handles technical support? Teacher documentation sufficient, or need help desk?

---

## Dependencies / Blockers

### External Dependencies
- **Claude API availability:** Tool depends on Anthropic API being operational
- **PythonAnywhere uptime:** Deployment relies on platform stability
- **Teacher feedback:** Need educator input to validate curriculum alignment before wider rollout

### Potential Blockers
- **API costs:** If Claude API usage becomes expensive, may need cost mitigation strategies
- **Curriculum changes:** If Ontario revises Grade 7-8 Language expectations, content needs updating
- **Privacy regulations:** May need legal review if deploying across multiple schools
- **Teacher capacity:** Adoption depends on teachers having time to learn new tool

### What We're Waiting On
- **User testing participants:** Need to recruit 2-3 Ontario teachers for feedback
- **Student testing opportunity:** Need parental consent and teacher partnership for student usability testing
- **Curriculum validation:** Ideally get review from Ontario curriculum specialist or EQAO expert

---

## Context for Next Session

### Where We Left Off
Completed MVP deployment to PythonAnywhere. All core features are implemented:
- Flask application structure
- Reading assessments with 4 themed passages
- Writing assessments with AI-powered feedback
- Student guides for reading and writing strategies
- Teacher guide with detailed rubrics and curriculum mappings
- GitHub repository configured
- Live at https://spartacu3131.pythonanywhere.com

**The WSGI configuration on PythonAnywhere was the last setup step completed.**

### Why We Made Key Decisions

**Flask over Django:**
- Simpler for single-purpose tool
- Easier PythonAnywhere deployment
- Less overhead, faster development
- Most appropriate for assessment-focused app

**"Think First" framework:**
- Pyramid Principle is powerful but sounds corporate/intimidating
- Grade 7-8 students respond better to "Think First" framing
- Maintains rigor while increasing accessibility
- Transferable skill that serves students beyond assessment

**AI for feedback, not grading:**
- Formative feedback supports learning
- Teachers retain grading authority (professional judgment)
- Reduces teacher workload on draft reviews
- Models constructive feedback language students can internalize

**No database in MVP:**
- Reduces complexity and deployment barriers
- Avoids student data privacy concerns
- Sufficient for assessment administration
- Can add later if progress tracking becomes priority

**Themed passages (Wagamese, Atwood, etc.):**
- Engages students through recognizable literary voices
- Provides cultural relevance and representation
- Exposes students to Canadian literature traditions
- Supports text-to-text connection skills across authors

### What to Tackle First

**Recommended starting point for next session:**

1. **Deploy verification** (30 minutes)
   - Open https://spartacu3131.pythonanywhere.com
   - Walk through complete user journey (reading assessment → writing assessment → view feedback)
   - Document any issues encountered
   - Fix critical bugs immediately if found

2. **Content expansion** (60-90 minutes)
   - Create 2 new reading passages (different themes than current 4)
   - Develop 6 new writing prompts (2 per genre)
   - Add to existing content structure
   - Map to curriculum expectations

3. **Teacher outreach** (30 minutes)
   - Identify 2-3 Ontario teachers to approach for feedback
   - Draft outreach message explaining project
   - Schedule user testing sessions
   - Prepare testing protocol and feedback form

**Why this order:**
- Verify deployment works before investing more development time
- Expand content while tool is fresh in mind
- Get user feedback early to guide future development priorities

**Estimated time commitment:** 2-3 hours for immediate next steps

---

## Future Enhancements (Not Immediate Priority)

### Phase 2 Features
- Student progress dashboard (requires database)
- Teacher admin panel (manage students, view aggregate data)
- Differentiated passage versions (same theme, varied complexity)
- Text-to-speech integration for accessibility
- Peer review workflow (students review each other's writing)

### Phase 3 Features
- Adaptive questioning (adjust difficulty based on performance)
- Portfolio system (students collect best work)
- Parent communication (share progress summaries)
- Research partnership (validate effectiveness empirically)
- Content marketplace (teachers share/purchase passages and prompts)

### Technical Debt to Address Later
- Unit test coverage (currently no tests)
- API error handling improvements
- Caching for API responses (reduce costs)
- Performance optimization (if usage scales)
- Accessibility audit (WCAG AA compliance)

---

## Success Indicators

**How we'll know next session is successful:**

1. Deployment is stable and functional (no critical bugs)
2. At least 2 new reading passages created
3. At least 6 new writing prompts added
4. Teacher outreach initiated (2-3 contacts made)
5. TODO list updated based on testing findings

**Red flags to watch for:**
- API failures or slow response times (>10 seconds)
- Content quality concerns (passages too hard/easy, prompts unclear)
- Technical errors on mobile devices
- Teacher confusion about rubrics or administration

---

## Resources & References

### Ontario Curriculum Documents
- Ontario Language Curriculum, Grades 1-8 (2006)
- EQAO assessment frameworks
- Growing Success: Assessment, Evaluation, and Reporting (2010)

### Technical Documentation
- Flask Documentation: https://flask.palletsprojects.com/
- Anthropic API Docs: https://docs.anthropic.com/
- PythonAnywhere Help: https://help.pythonanywhere.com/

### Educational Resources
- Barbara Minto: "The Pyramid Principle" (structured thinking)
- Reading comprehension strategy research
- Writing assessment rubric design
- Formative feedback best practices

### Project Links
- Live App: https://spartacu3131.pythonanywhere.com
- GitHub Repo: https://github.com/justinholmes-7shifts/ontario-reading-assessment
- Session Summary: `ontario-reading-assessment-session-summary.md`
- AI Context: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`

---

## Notes

- Remember to test on actual mobile devices, not just browser responsive mode
- Keep passage reading level at Grade 7-8 (Flesch-Kincaid check)
- All new content must include curriculum expectation codes
- Student guides should be updated when new assessment types added
- Teacher guide needs sample responses for new prompts

**Most important:** Get teacher feedback BEFORE scaling up. They'll catch curriculum alignment issues and usability problems students might not articulate.
