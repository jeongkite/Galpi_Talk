let chapArray = ['/privacy/', '/talk/chap/1/', '/talk/chap/2/', '/talk/chap/3/', '/talk/chap/4/', '/talk/chap5/',]

var chapter_ani_1 = bodymovin.loadAnimation({
    container: document.getElementById('chapter_ani_1'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/chapter1.json',
});
var chapter_ani_2 = bodymovin.loadAnimation({
    container: document.getElementById('chapter_ani_2'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/chapter2.json'
});
var chapter_ani_3 = bodymovin.loadAnimation({
    container: document.getElementById('chapter_ani_3'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/chapter3.json'
});
var chapter_ani_4 = bodymovin.loadAnimation({
    container: document.getElementById('chapter_ani_4'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/chapter4.json'
});
var chapter_ani_5 = bodymovin.loadAnimation({
    container: document.getElementById('chapter_ani_5'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/chapter5.json'
});


var main_ani = bodymovin.loadAnimation({
    container: document.getElementById('lottie_main'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/Main.json'
});
var question_ani = bodymovin.loadAnimation({
    container: document.getElementById('lottie_question'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/Question.json'
});
var final_ani = bodymovin.loadAnimation({
    container: document.getElementById('lottie_final'),
    renderer: 'svg',
    loop: false,
    autoplay: true,
    path: '/static/js/animation/Final.json'
});

chapter_ani_1.addEventListener('complete', function () {
    location.href = '/talk/chap/1/'
});
chapter_ani_2.addEventListener('complete', function () {
    location.href = '/talk/chap/2/'
})
chapter_ani_3.addEventListener('complete', function () {
    location.href = '/talk/chap/3/'
})
chapter_ani_4.addEventListener('complete', function () {
    location.href = '/talk/chap/4/'
})
chapter_ani_5.addEventListener('complete', function () {
    location.href = '/talk/chap5/'
})

function chap_back(chap) {
    location.href = chapArray[chap - 1];
}
function chap_next(chap) {
    location.href = chapArray[chap + 1];
}

function countLength(tags, maxLength) {
    document.getElementById("limit").value = (maxLength - tags.value.length);
}

window.onload = function () {
    let last = document.getElementById("last");
    last.scrollIntoView();
}