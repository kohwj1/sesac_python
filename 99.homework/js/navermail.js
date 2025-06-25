const all_checkbox = document.querySelectorAll('.button_checkbox');
const mail_list = document.querySelectorAll('.button_sender');

for (item of all_checkbox) {
    item.checked = true;
};

for (sender of mail_list) {
    idx = sender.title.indexOf('<');
    console.log(sender.title.slice(idx + 1, -1));
};