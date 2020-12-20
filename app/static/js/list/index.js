const trigger = document.querySelectorAll('.js--trigger');

[].slice.call(trigger).forEach(element => {
  element.addEventListener('click', () => {

    const firstChildElement = element.firstElementChild;
    const iconElement = firstChildElement.lastElementChild;
    const lastChildElement = element.lastElementChild;
    console.log(firstChildElement);
    console.log(lastChildElement);


    iconElement.classList.toggle('is-rotate');
    lastChildElement.classList.toggle('is-active');

  });
});