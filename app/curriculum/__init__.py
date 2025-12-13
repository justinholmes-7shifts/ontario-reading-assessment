# Ontario Curriculum Data for Grade 7-8 Language

READING_EXPECTATIONS = {
    "grade_7": {
        "comprehension": {
            "code": "1.1-1.9",
            "description": "Read and demonstrate understanding of texts",
            "skills": [
                "Identify purpose and intended audience",
                "Use comprehension strategies (predicting, questioning, visualizing)",
                "Demonstrate understanding of content, form, and style",
                "Make inferences using stated and implied ideas",
                "Extend understanding through discussion and writing",
                "Analyze texts for bias and perspective",
                "Identify point of view and evaluate evidence",
                "Analyze media texts for techniques and purposes"
            ]
        },
        "critical_literacy": {
            "code": "1.5-1.7",
            "description": "Analyze and evaluate texts critically",
            "skills": [
                "Identify perspectives and biases",
                "Evaluate credibility of sources",
                "Recognize persuasive techniques",
                "Compare different texts on same topic"
            ]
        },
        "vocabulary": {
            "code": "1.8",
            "description": "Use vocabulary acquisition strategies",
            "skills": [
                "Use context clues to determine meaning",
                "Recognize word roots, prefixes, suffixes",
                "Use dictionaries and thesauruses effectively"
            ]
        }
    },
    "grade_8": {
        "comprehension": {
            "code": "1.1-1.9",
            "description": "Read and demonstrate understanding of increasingly complex texts",
            "skills": [
                "Identify purpose, audience, and form",
                "Apply deep comprehension strategies",
                "Synthesize ideas from multiple texts",
                "Make complex inferences",
                "Analyze how form and style support meaning",
                "Evaluate arguments and identify logical fallacies",
                "Analyze author's craft and purpose",
                "Critically analyze media texts"
            ]
        },
        "critical_literacy": {
            "code": "1.5-1.7",
            "description": "Critically analyze and evaluate texts",
            "skills": [
                "Identify and analyze perspectives",
                "Evaluate validity and reliability",
                "Recognize and analyze persuasive techniques",
                "Synthesize information from varied sources"
            ]
        },
        "vocabulary": {
            "code": "1.8",
            "description": "Expand vocabulary through various strategies",
            "skills": [
                "Use sophisticated context clues",
                "Apply knowledge of etymology",
                "Use academic and domain-specific vocabulary"
            ]
        }
    }
}

WRITING_EXPECTATIONS = {
    "grade_7": {
        "developing_ideas": {
            "code": "1.1-1.6",
            "description": "Generate, gather, and organize ideas",
            "skills": [
                "Generate ideas using various strategies",
                "Establish clear focus and purpose",
                "Gather information from various sources",
                "Organize ideas logically with clear structure",
                "Use paragraphs effectively",
                "Review and revise for content and organization"
            ]
        },
        "form_and_style": {
            "code": "2.1-2.8",
            "description": "Use knowledge of form and style",
            "skills": [
                "Write for different purposes and audiences",
                "Use appropriate voice and tone",
                "Use varied sentence structures",
                "Use literary devices effectively",
                "Choose words precisely",
                "Maintain consistent point of view"
            ]
        },
        "conventions": {
            "code": "3.1-3.8",
            "description": "Apply conventions of standard English",
            "skills": [
                "Use correct spelling",
                "Use punctuation correctly",
                "Use grammar conventions correctly",
                "Use capitalization correctly",
                "Proofread and edit for errors"
            ]
        }
    },
    "grade_8": {
        "developing_ideas": {
            "code": "1.1-1.6",
            "description": "Generate, gather, and organize complex ideas",
            "skills": [
                "Generate sophisticated ideas",
                "Establish compelling focus and clear thesis",
                "Research and synthesize from multiple sources",
                "Organize ideas with sophisticated transitions",
                "Use complex paragraph structures",
                "Revise for clarity, coherence, and impact"
            ]
        },
        "form_and_style": {
            "code": "2.1-2.8",
            "description": "Apply sophisticated knowledge of form and style",
            "skills": [
                "Adapt writing for various purposes and audiences",
                "Establish and maintain authentic voice",
                "Use varied and complex sentence structures",
                "Use literary devices with sophistication",
                "Choose precise and vivid language",
                "Maintain consistent and appropriate tone"
            ]
        },
        "conventions": {
            "code": "3.1-3.8",
            "description": "Apply conventions with increasing accuracy",
            "skills": [
                "Spell complex words correctly",
                "Use advanced punctuation correctly",
                "Apply complex grammar rules",
                "Use conventions to enhance meaning",
                "Edit thoroughly for correctness"
            ]
        }
    }
}

# Ontario Achievement Chart Levels
ACHIEVEMENT_LEVELS = {
    "level_1": {
        "range": "50-59%",
        "description": "Limited achievement of expectations",
        "characteristics": "Demonstrates limited understanding with significant gaps"
    },
    "level_2": {
        "range": "60-69%",
        "description": "Some achievement of expectations",
        "characteristics": "Demonstrates some understanding with some gaps"
    },
    "level_3": {
        "range": "70-79%",
        "description": "Considerable achievement of expectations",
        "characteristics": "Demonstrates considerable understanding meeting provincial standard"
    },
    "level_4": {
        "range": "80-100%",
        "description": "High achievement of expectations",
        "characteristics": "Demonstrates thorough understanding exceeding provincial standard"
    }
}

# Writing Rubric based on Ontario Achievement Chart
WRITING_RUBRIC = {
    "ideas_content": {
        "weight": 25,
        "criteria": {
            4: "Ideas are insightful, original, and fully developed with rich details",
            3: "Ideas are clear, focused, and well-developed with relevant details",
            2: "Ideas are present but may lack focus or sufficient development",
            1: "Ideas are unclear, unfocused, or minimally developed"
        }
    },
    "organization": {
        "weight": 25,
        "criteria": {
            4: "Exceptional organization with sophisticated transitions and logical flow",
            3: "Clear organization with effective transitions and coherent structure",
            2: "Some organization present but may have weak transitions or unclear structure",
            1: "Little or no organization; difficult to follow"
        }
    },
    "voice_style": {
        "weight": 25,
        "criteria": {
            4: "Distinctive voice; sophisticated word choice and varied sentences",
            3: "Appropriate voice; effective word choice and sentence variety",
            2: "Inconsistent voice; limited word choice or sentence variety",
            1: "No clear voice; basic word choice and repetitive sentences"
        }
    },
    "conventions": {
        "weight": 25,
        "criteria": {
            4: "Virtually no errors; enhances meaning through conventions",
            3: "Few errors that don't impede understanding",
            2: "Some errors that may impede understanding",
            1: "Frequent errors that significantly impede understanding"
        }
    }
}
