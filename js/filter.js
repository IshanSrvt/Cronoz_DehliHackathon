function filterItems() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('search-bar');
    filter = input.value.toUpperCase();
    ul = document.getElementById('item-list');
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = '';
        } else {
            li[i].style.display = 'none';
        }
    }
}
