const sidebarEl = document.querySelector(".sidebar");
const sidebarBtn = document.querySelector(".sidebar-btn");

sidebarBtn.addEventListener("click", () => {
  sidebarEl.classList.toggle('sidebar-in')
});