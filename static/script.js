
function changeMethodVisibility(option) {
    if (option == 'readability') {
        // text content div
        document.getElementById('method-text-readability').classList.remove('mt-hide');
        document.getElementById('method-text-similarity').classList.add('mt-hide');
        // title style - colors and border-bottom
        document.getElementById('method-title-readability').classList.remove('mt-inactive');
        document.getElementById('method-title-similarity').classList.add('mt-inactive');
        document.getElementById('method-title-span-readability').classList.add('ed');
        document.getElementById('method-title-span-similarity').classList.remove('ed');



    } else {
        // text content div
        document.getElementById('method-text-readability').classList.add('mt-hide');
        document.getElementById('method-text-similarity').classList.remove('mt-hide');
        // title style - colors and border-bottom
        document.getElementById('method-title-readability').classList.add('mt-inactive');
        document.getElementById('method-title-similarity').classList.remove('mt-inactive');
        document.getElementById('method-title-span-readability').classList.remove('ed');
        document.getElementById('method-title-span-similarity').classList.add('ed');
    }
}