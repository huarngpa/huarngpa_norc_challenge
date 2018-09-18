<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ name }}</h2>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="tabs is-centered is-fullwidth is-large">
          <ul>
            <li :class="{'is-active': step == 'name'}" @click="step = 'name'">
              <a>Name</a>
            </li>
            <li :class="{'is-active': step == 'questions'}" @click="step = 'questions'">
              <a>Questions</a>
            </li>
            <li :class="{'is-active': step == 'review'}" @click="step = 'review'">
              <a>Review</a>
            </li>
          </ul>
        </div>
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <div class="name" v-show="step === 'name'">
              <div class="field">
                <label class="label" for="name">Survey name:</label>
                <div class="control">
                  <input type="text" class="input is-large" id="name" v-model="name">
                </div>
              </div>
            </div>
            <div class="questions" v-show="step === 'questions'">
              <new-question @questionComplete="appendQuestion"/>
            </div>
            <div class="review" v-show="step === 'review'">
              <h2>Review and Submit</h2>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
    </section>
  </div>
</template>

<script>
import NewQuestion from '@/components/NewQuestion'

export default {
  components: { NewQuestion },
  data() {
    return {
      step: 'name',
      name: '',
      questions: []
    }
  },
  methods: {
    appendQuestion(newQuestion) {
      this.question.push(newQuestion)
    }
  },
}
</script>

<style></style>
