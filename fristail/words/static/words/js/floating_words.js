const floating_words_canvas = document.getElementById("floating_words_canvas");
const floating_words_ctx = floating_words_canvas.getContext("2d");

const floating_words_li = document.getElementsByClassName("floating_word");
const floating_words = []
for (let i = 0; i < floating_words_li.length; i++) {
    floating_words.push(floating_words_li.item(i).innerText);
}

const floating_words_colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"];

const floating_words_font_size = 20;
const floating_words_font_family = "Arial";
const floating_words_font = floating_words_font_size + "px " + floating_words_font_family;

const floating_words_speed = 1;

var last_floating_word = "";
var last_floating_word_x = 0;
var last_floating_word_y = 0;

var floating_words_count = 0;
const MAX_FLOATING_WORDS = 100;

function show_floating_word() {
    let floating_word = floating_words[Math.floor(Math.random() * floating_words.length)];
    while (floating_word == last_floating_word) {
        floating_word = floating_words[Math.floor(Math.random() * floating_words.length)];
    }
    let floating_word_x = Math.floor(Math.random() * (floating_words_canvas.width - floating_words_ctx.measureText(floating_word).width));
    let floating_word_y = Math.floor(Math.random() * (floating_words_canvas.height - floating_words_font_size));
    while (
        Math.abs(floating_word_x - last_floating_word_x) < floating_words_ctx.measureText(floating_word).width &&
        Math.abs(floating_word_y - last_floating_word_y) < floating_words_font_size &&
        (floating_word_x != last_floating_word_x || floating_word_y != last_floating_word_y)
        ) {
        floating_word_x = Math.floor(Math.random() * (floating_words_canvas.width - floating_words_ctx.measureText(floating_word).width));
        floating_word_y = Math.floor(Math.random() * (floating_words_canvas.height - floating_words_font_size));
    }
    last_floating_word = floating_word;
    if (floating_words_count >= MAX_FLOATING_WORDS) {
        floating_words_ctx.clearRect(0, 0, floating_words_canvas.width, floating_words_canvas.height);
    }
    floating_words_ctx.font = floating_words_font;
    floating_words_ctx.fillStyle = floating_words_colors[Math.floor(Math.random() * floating_words_colors.length)];
    floating_words_ctx.fillText(floating_word, floating_word_x, floating_word_y);

    setTimeout(show_floating_word, 1000);
}

show_floating_word();
