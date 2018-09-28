import axios from "axios";

//axios.defaults.xsrfCookieName = 'csrftoken'
//axios.defaults.xsrfHeaderName = 'X-CSRFToken'

//const API_URL = "https://huarngpa.com";
const API_URL = "http://localhost:8000";

export function fetchSurveys(jwt) {
  return axios.get(`${API_URL}/djangobasic/api/survey/`, {
    headers: {
      'Authorization': `Bearer ${jwt}`,
    }
  });
}

export function fetchSurvey(jwt, surveyId) {
  return axios.get(`${API_URL}/djangobasic/api/survey/{surveyId}/`, {
    headers: {
      'Authorization': `Bearer ${jwt}`,
    }
  });
}

export function saveSurveyResponse(jwt, surveyResponse) {
  // TODO
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("Saving survey response...");
      resolve();
    }, 300);
  });
}

export function postNewSurvey(jwt, survey) {
  // TODO
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("Saving survey...", survey);
      resolve();
    }, 300);
  });
}

export function authenticate(userData) {
  return axios.post(`${API_URL}/api-token-auth/`, userData);
}

export function register(userData) {
  return axios.post(`${API_URL}/signup/`, userData);
}

//const surveys = [{
//    id: 1,
//    name: 'Postsecondary Education',
//    created_at: new Date(2018, 9, 4),
//    questions: [{
//        id: 1,
//        text: 'What was your GPA (postsecondary) out of a 4.0-scale?',
//        choices: [{
//            id: 1,
//            text: 'Not Applicable',
//            selected: 0
//        }, {
//            id: 2,
//            text: '0.0 - 1.0',
//            selected: 0
//        }, {
//            id: 3,
//            text: '1.0 - 1.5',
//            selected: 0
//        }, {
//            id: 4,
//            text: '1.5 - 2.0',
//            selected: 0
//        }, {
//            id: 5,
//            text: '2.0 - 2.5',
//            selected: 0
//        }, {
//            id: 6,
//            text: '2.5 - 3.0',
//            selected: 0
//        }, {
//            id: 7,
//            text: '3.0 - 3.5',
//            selected: 0
//        }, {
//            id: 8,
//            text: '3.5 - 4.0',
//            selected: 0
//        }, ]
//    }, {
//        id: 2,
//        text: 'What kind of postsecondary education do you have?',
//        choices: [{
//            id: 9,
//            text: 'None',
//            selected: 0
//        }, {
//            id: 10,
//            text: 'Two-Year Community College',
//            selected: 0
//        }, {
//            id: 11,
//            text: 'Four-Year College or University',
//            selected: 0
//        }, {
//            id: 12,
//            text: 'Graduate or PhD',
//            selected: 0
//        }, ]
//    }, ]
//}]
//
//export function fetchSurveys() {
//    return new Promise((resolve, reject) => {
//        setTimeout(() => {
//            resolve(surveys)
//        }, 300) // simulate delay
//    })
//}
//
//export function fetchSurvey(surveyId) {
//    return new Promise((resolve, reject) => {
//        setTimeout(() => {
//            const survey = surveys.find(survey => survey.id === surveyId)
//            if (survey) {
//                resolve(survey)
//            } else {
//                reject(Error('Survey does not exist'))
//            }
//        }, 300) // simulate delay
//    })
//}
//
//export function saveSurveyResponse(surveyResponse) {
//    return new Promise((resolve, reject) => {
//        setTimeout(() => {
//            console.log('Saving survey response...')
//            resolve()
//        }, 300)
//    })
//}
//
//export function postNewSurvey(survey) {
//    return new Promise((resolve, reject) => {
//        setTimeout(() => {
//            console.log('Saving survey...', survey)
//            resolve()
//        }, 300)
//    })
//}
