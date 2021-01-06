const trigger = document.querySelectorAll('.js--trigger');

[].slice.call(trigger).forEach(element => {
  element.addEventListener('click', () => {

    // ハンバーガーメニューの取得
    const firstChildElement = element.firstElementChild;
    // 隠れてる × を取得
    const lastChildElement = element.lastElementChild;
    // 隠れてるメニューを取得
    const sibling = element.nextElementSibling;

    sibling.classList.toggle('is--open');
    lastChildElement.classList.toggle('is--open');
    firstChildElement.classList.toggle('is--hide')
  });
});