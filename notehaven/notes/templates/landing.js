import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js';
const Card = {
  template:`<div class="card">
    <i v-bind:class="clss"></i>
    <p class="card-text">{{text}}
</p>
  </div>`,
  props:{
    clss:{
      type:String,
      required: true,
    },
    text:{
      type:String,
      required: true,
    }
    
  },
  mounted(){
    window.addEventListener('scroll', () => {
    const elements = document.querySelectorAll('.card');
    elements.forEach((element) => {
    const rect = element.getBoundingClientRect();
    if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
        document.querySelector('.nav-bar').style.backgroundColor = "#9F5255";
    }else{
      document.querySelector('.nav-bar').style.backgroundColor = "#E16A14";
    }
    });
});
  const icons = document.querySelectorAll('i');
  icons.forEach(icon => {
    icon.addEventListener('click',() =>{
      icon.style.transform = 'scale(1.3)'
    });
    
  });
  const startBtn = document.querySelector('.start-btn');
  startBtn.addEventListener('click',()=>{
    document.location.href = 'home.html'
  })
  }
}

const app = createApp({});
app.component('card',Card);
app.mount('#app');


