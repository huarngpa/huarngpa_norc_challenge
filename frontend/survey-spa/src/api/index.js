const surveys = [{
    id: 1,
    name: 'Postsecondary Education',
    created_at: new Date(2018, 9, 4),
    questions: [{
        id: 1,
        text: 'What was your GPA (postsecondary) out of a 4.0-scale?',
        choices: [{
            id: 1,
            text: 'Not Applicable',
            selected: 0
        }, {
            id: 2,
            text: '0.0 - 1.0',
            selected: 0
        }, {
            id: 3,
            text: '1.0 - 1.5',
            selected: 0
        }, {
            id: 4,
            text: '1.5 - 2.0',
            selected: 0
        }, {
            id: 5,
            text: '2.0 - 2.5',
            selected: 0
        }, {
            id: 6,
            text: '2.5 - 3.0',
            selected: 0
        }, {
            id: 7,
            text: '3.0 - 3.5',
            selected: 0
        }, {
            id: 8,
            text: '3.5 - 4.0',
            selected: 0
        }, ]
    }, {
        id: 2,
        text: 'What kind of postsecondary education do you have?',
        choices: [{
            id: 9,
            text: 'None',
            selected: 0
        }, {
            id: 10,
            text: 'Two-Year Community College',
            selected: 0
        }, {
            id: 11,
            text: 'Four-Year College or University',
            selected: 0
        }, {
            id: 12,
            text: 'Graduate or PhD',
            selected: 0
        }, ]
    }, ]
}]

export function fetchSurveys(surveyId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const survey = surveys.find(survey => survey.id === surveyId)
            if (survey) {
                resolve(survey)
            } else {
                reject(Error('Survey does not exist'))
            }
        }, 300) // simulate delay
    })
}
