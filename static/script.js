document.addEventListener("DOMContentLoaded", function () {
  const outputLang = document.querySelector("select[name='output_lang']");
  const textarea = document.querySelector("textarea");

  function updateFont() {
    textarea.classList.remove("english", "hindi", "japanese", "kannada");

    if (outputLang.value === "en") {
      textarea.classList.add("english");
    } else if (outputLang.value === "hi") {
      textarea.classList.add("hindi");
    } else if (outputLang.value === "ja") {
      textarea.classList.add("japanese");
    } else if (outputLang.value === "kn") {
      textarea.classList.add("kannada");
    }
  }
  function scrollToForm() {
    document.getElementById("mainForm").scrollIntoView({
      behavior: "smooth",
    });
  }

  outputLang.addEventListener("change", updateFont);
});
