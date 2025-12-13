from flask import Blueprint, render_template, request, jsonify, session
from app.assessments.reading import ReadingAssessment
from app.assessments.writing import WritingAssessment

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/reading')
def reading_assessment():
    assessment = ReadingAssessment()
    passages = assessment.get_available_passages()
    return render_template('reading.html', passages=passages)


@main.route('/reading/<passage_id>')
def reading_test(passage_id):
    assessment = ReadingAssessment()
    passage_data = assessment.get_passage(passage_id)
    if not passage_data:
        return "Passage not found", 404
    return render_template('reading_test.html', passage=passage_data)


@main.route('/reading/submit', methods=['POST'])
def submit_reading():
    data = request.json
    assessment = ReadingAssessment()
    results = assessment.evaluate_answers(data['passage_id'], data['answers'])
    return jsonify(results)


@main.route('/writing')
def writing_assessment():
    assessment = WritingAssessment()
    prompts = assessment.get_available_prompts()
    return render_template('writing.html', prompts=prompts)


@main.route('/writing/<prompt_id>')
def writing_test(prompt_id):
    assessment = WritingAssessment()
    prompt_data = assessment.get_prompt(prompt_id)
    if not prompt_data:
        return "Prompt not found", 404
    return render_template('writing_test.html', prompt=prompt_data)


@main.route('/writing/submit', methods=['POST'])
def submit_writing():
    data = request.json
    assessment = WritingAssessment()
    results = assessment.evaluate_writing(data['prompt_id'], data['response'])
    return jsonify(results)


@main.route('/results')
def results():
    return render_template('results.html')
