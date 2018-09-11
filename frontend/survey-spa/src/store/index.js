import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  // single source of data
  surveys: []
};

const actions = {
  // asynchronous operations
};

const mutations = {
  // isolated data mutations
};

const getters = {
  // resusable data accessors
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
});
