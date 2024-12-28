<template>
  <div class="app">
    <nav class="navbar">
      <div class="center-links">
        <router-link to="/">Home</router-link>
        <router-link to="/info">Info</router-link>
        <router-link to="/cv">Computer Vision</router-link>
        <router-link to="/tg">Text Generation</router-link>
      </div>
    </nav>

    <div class="page-content">
      <router-view />
    </div>

    <footer class="site-footer">
      <p>Created by Andrii Slyva</p>
      <div class="social-links">
        <a href="https://www.instagram.com/slivandrii14" target="_blank">
          <img
            src="@/assets/images/instagram.png"
            alt="Instagram"
            class="logo-instagram"
          />
        </a>
        <a href="https://t.me/kitotp" target="_blank">
          <img
            src="@/assets/images/telegram.png"
            alt="Telegram"
            class="logo-telegram"
          />
        </a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  font-family: 'Kanit', sans-serif;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; 
}

nav {
  display: flex;
  width:100%;
  height: 50px;
  align-items: center;
  justify-content: space-between;
  background-color: black;
}

.center-links{
  display: flex;
  justify-content: center;
  gap: 20px;
  flex: 1;
}

.navbar a {
  color: #b3b3b3;
  text-decoration: none;
  font-size: 1rem;
  padding: 8px 16px;
  border-radius: 6px;
  transition: background-color 0.3s, color 0.3s;
  border: 1px solid transparent;
}

.navbar a:hover {
  color: #ffffff;
  background-color: rgba(255, 255, 255, 0.1);
  border-color: #4e0099;
}

.navbar a:active {
  color: #4e0099;
}

/* FOOTER  */
.site-footer {
  width: 100%;
  background-color: #000000;
  color: #ffffff;
  text-align: center;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.site-footer p {
  margin: 0;
  font-size: 1.2vw;
  margin-left: 2%;
}

.social-links {
  display: flex;
  gap: 20px;
  margin-right: 1%;
}

.logo-instagram,
.logo-telegram {
  width: 30px;
  height: 30px;
}
</style>
