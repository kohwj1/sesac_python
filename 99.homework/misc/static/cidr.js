let is_tooltip_visible = false;

tooltip = document.getElementById('tooltipHelp');
document.getElementById('icoHelp').addEventListener('click', () => {
    if (is_tooltip_visible) {
        tooltip.style.display = 'none';
    } else {
        tooltip.style.display = 'block';
    }
    
    is_tooltip_visible = !is_tooltip_visible
})