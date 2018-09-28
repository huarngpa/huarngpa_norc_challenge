<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
            <h2 class="title">{{ survey.name }}</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="columns">
          <div>

            <div
              v-for="(question, idx) in survey.questions"
              v-bind:key="question.id"
              v-show="currentQuestion === idx">

              <div class="column has-text-centered">
                <h4 class="title has-text-centered">{{ question.question_text }}</h4>
              </div>

              <div class="column has-text-centered">
                <div class="control">
                  <div v-for="choice in question.choices" @key="choice.id">
                    <label class="radio">
                      <input type="radio" v-model="question.choice" :value="choice.id">
                      {{ choice.choice_text }}</label>
                  </div>
                </div>
              </div>

            </div>

            <!-- Pagination buttons -->
            <div class="column is-offset-one-quarter is-half">
              <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                  <a class="pagination-previous" @click.stop="goToPreviousQuestion"><i class="fa fa-chevron-left" aria-hidden="true"></i>&nbsp;&nbsp; Back</a>
                  <a class="pagination-next" @click.stop="goToNextQuestion">&nbsp;&nbsp; Next<i class="fa fa-chevron-right" aria-hidden="true"></i></a>
              </nav>
            </div>

            <!-- Submit -->
            <div class="column has-text-centered">
              <a v-if="surveyCompleted" class="button is-focused is-primary is-large"
                @click.stop="handleSubmit">Submit</a>
            </div>

          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentQuestion: 0
    };
  },
  beforeMount() {
    this.$store.dispatch('loadSurvey', { id: parseInt(this.$route.params.id) })
  },
  methods: {
    goToNextQuestion() {
      if (this.currentQuestion === this.survey.questions.length - 1) {
        this.currentQuestion = 0;
      } else {
        this.currentQuestion++;
      }
    },
    goToPreviousQuestion() {
      if (this.currentQuestion === 0) {
        this.currentQuestion = this.survey.questions.length - 1;
      } else {
        this.currentQuestion--;
      }
    },
    handleSubmit() {
      this.$store.dispatch('addSurveyResponse')
        .then(() => this.$router.push('/'))
    }
  },
  computed: {
    surveyCompleted() {
      if (this.survey.questions) {
        const numQuestions = this.survey.questions.length;
        const numCompleted = this.survey.questions.filter(q => q.choice).length;
        return numQuestions === numCompleted;
      }
      return false;
    },
    survey() {
      return this.$store.state.currentSurvey
    },
    selectedChoice: {
      get() {
        const question = this.survey.questions[this.currentQuestion]
        return question.choice
      },
      set(value) {
        const question = this.survey.questions[this.currentQuestion]
        this.$store.commit('setChoice', { questionId: question.id, choice: value })
      }
    }
  }
};
</script>

<style>
</style>
