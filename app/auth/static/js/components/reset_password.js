import ResetPasswordTemplate from "../templates/reset_password.template.js";

const ResetPassword = {
  data () {
    return {
      resetSuccess: false,
      gotToken: false,
      errors: {},
      formData: {
        username: "",
        token: "",
        password: "",
        password2: "",
      }
    }
  },

  methods: {
    processForm() {
      if (this.validate()) this.gotToken ? this.reset() : this.request()
    },

    validate() {
      const vm = this; //current vue instance;
      this.errors = {}
      const formId = 'validated-form';
      let nodes = document.querySelectorAll(`#${formId} :invalid`);

      if (this.formData.password2 != this.formData.password)
         this.errors['password2'] = 'Passwords must match'

      if (nodes.length > 0 || this.errors['password2']) {
        nodes.forEach(node => {
          this.errors[node.name] = node.validationMessage
          node.addEventListener('change', function (e) {
            vm.validate()
          })
        })
        return false
      }
      return true
    },

    request() {
      wretch("/auth/reset_password_request")
        .post(this.formData)
        .json(json => {
          console.log(json)
          this.errors = { ...this.errors, 'server': json.message}
          if (json.ok) this.gotToken=true
        })
        .catch(error => {console.log(error)})
    },

    reset() {
      wretch("/auth/reset_password")
        .post(this.formData)
        .json(json => {
          console.log(json)
          this.errors = { ...this.errors, 'server': json.message}
          if (json.ok) this.resetSuccess=true
        })
        .catch(error => {console.log(error)})
    },
  },
    template: ResetPasswordTemplate,
}

export default ResetPassword
