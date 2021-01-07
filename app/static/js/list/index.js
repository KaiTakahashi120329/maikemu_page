const listTrigger = document.querySelectorAll('.js--trigger-list');

[].slice.call(listTrigger).forEach(element => {
  element.addEventListener('click', () => {

    // 対象の要素取得
    const firstChildElement = element.firstElementChild;
    // アイコン要素取得
    const iconElement = firstChildElement.lastElementChild;
    // 隠れている要素取得
    const lastChildElement = element.lastElementChild;

    iconElement.classList.toggle('is-rotate');
    lastChildElement.classList.toggle('is-active');

  });
});