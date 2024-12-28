<template>
    <div class="home-wrapper">
      <div class="section" id="section1">
        <div class="autotype">
          <p>Explore the <span class="auto-type"></span></p>
        </div>
      </div>
  
      <!-- Блок Computer Vision -->
      <div class="section" id="section2">
        <div class="content">
          <div class="content-item">
            <h1 class="title">Computer Vision</h1>
            <p class="description">
              Try a cutting-edge technology that allows machines to interpret
              and understand the visual world. By analyzing images and videos,
              computer vision systems can identify objects, detect faces, and
              comprehend scenes and activities.
            </p>
  
            <router-link to="/cv">
              <button>
                Try Now
                <div class="star-1">
                  <svg viewBox="0 0 784.11 815.53">
                    <path
                      class="fil0"
                      d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z"
                    />
                  </svg>
                </div>
                <div class="star-2">
                  <svg viewBox="0 0 784.11 815.53">
                    <path
                      class="fil0"
                      d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z"
                    />
                  </svg>
                </div>
                <div class="star-3">
                  <svg viewBox="0 0 784.11 815.53">
                    <path
                      class="fil0"
                      d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z"
                    />
                  </svg>
                </div>
                <div class="star-4">
                  <svg viewBox="0 0 784.11 815.53">
                    <path
                      class="fil0"
                      d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z"
                    />
                  </svg>
                </div>
                <div class="star-5">
                  <svg viewBox="0 0 784.11 815.53">
                    <path
                      class="fil0"
                      d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z"
                    />
                  </svg>
                </div>
                <div class="star-6">
                  <svg viewBox="0 0 784.11 815.53">
                    <path
                      class="fil0"
                      d="M392.05 0c-20.9,210.08 -184.06,378.41 -392.05,407.78 207.96,29.37 371.12,197.68 392.05,407.74 20.93,-210.06 184.09,-378.37 392.05,-407.74 -207.98,-29.38 -371.16,-197.69 -392.06,-407.78z"
                    />
                  </svg>
                </div>
              </button>
            </router-link>
          </div>
  
          <div class="content-item">
            <img src="@/assets/images/cv2.gif" alt="cvgif" class="cvgif" />
            <p>Mask-RCNN doing object detection and instance segmentation</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import Typed from 'typed.js'
  
  onMounted(() => {
    new Typed('.auto-type', {
      strings: ['future', 'creativity', 'magic', 'abilities', 'AI.'],
      typeSpeed: 80,
      backSpeed: 80,
      loop: false
    })
  })
  </script>
  
  <style scoped>
.home-wrapper{
    color:white;
    background-image: url('@/assets/images/bg-cv.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

  .section {
    width: 100%;
    display: flex;
    align-items: center;
    position: relative;
  }
  
  #section1 {
    height: 100vh;
  }
  
  #section2 {
    height: 60vh;
    padding-bottom: 7vw;
  }
  
  .content {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 5%;
  }
  
  .content-item {
    width: 45%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  /* Текст "Explore the ..." */
  .autotype {
    width: 100%;
    height: 100vh;
    font-weight: 600;
    background-color: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 6vw;
  }
  
  .auto-type {
    color: #ff7f50;
  }
  
  /* Заголовки, описания */
  .title {
    font-size: 5vw;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .description {
    font-size: 1vw;
    text-align: center;
    margin-bottom: 2vw;
  }
  
  /* Картинка (GIF) */
  .cvgif {
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    transition: transform 0.5s, box-shadow 0.5s;
    margin-top: 6vw;
    width: 100%;
    max-width: 600px;
    height: auto;
  }
  
  .cvgif:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.7);
  }
  
  /* try now */
  button {
    position: relative;
    padding: 12px 35px;
    background: #ffffff;
    font-size: 17px;
    font-weight: 700;
    color: #181818;
    border: 3px solid #ffffff;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
    cursor: pointer;
  }
  
  /* STARS */
  .star-1, .star-2, .star-3,
  .star-4, .star-5, .star-6 {
    position: absolute;
    filter: drop-shadow(0 0 0 #fffdef);
    z-index: -5;
    width: 15px;
    transition: all 1s cubic-bezier(0, 0.4, 0, 1.01);
  }
  
  /* Индивидуальные размеры / позиционирование */
  .star-1 { top: 20%; left: 20%; width: 25px; }
  .star-2 { top: 45%; left: 45%; }
  .star-3 { top: 40%; left: 40%; width: 5px; }
  .star-4 { top: 20%; left: 40%; width: 8px; transition: all 0.8s; }
  .star-5 { top: 25%; left: 45%; }
  .star-6 { top: 5%;  left: 50%; width: 5px; transition: all 0.8s ease; }
  
  /* Hover-анимация */
  button:hover {
    background: transparent;
    color: #ec9d64;
    box-shadow: 0 0 25px #fec1958c;
  }
  
  button:hover .star-1 {
    top: -80%; left: -30%;
    filter: drop-shadow(0 0 10px #fffdef);
    z-index: 2;
  }
  button:hover .star-2 {
    top: -25%; left: 10%;
    filter: drop-shadow(0 0 10px #fffdef);
    z-index: 2;
  }
  button:hover .star-3 {
    top: 55%; left: 25%;
    filter: drop-shadow(0 0 10px #fffdef);
    z-index: 2;
  }
  button:hover .star-4 {
    top: 30%; left: 80%;
    filter: drop-shadow(0 0 10px #fffdef);
    z-index: 2;
  }
  button:hover .star-5 {
    top: 25%; left: 115%;
    filter: drop-shadow(0 0 10px #fffdef);
    z-index: 2;
  }
  button:hover .star-6 {
    top: 5%; left: 60%;
    filter: drop-shadow(0 0 10px #fffdef);
    z-index: 2;
  }
  
  .fil0 {
    fill: #fffdef;
  }
  </style>
  