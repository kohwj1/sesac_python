const open = document.getElementById('open');

open.onclick = () => {
    showModal();
}

function showModal() {
    //모달 컨테이너
    const modalWrapper = document.createElement('div');
    modalWrapper.className = 'modal-wrapper';
    
    //모달 html
    modalWrapper.innerHTML = `
    <div class="modal-wrapper">
        <div class="modal">
            <div class="modal-title">모달 제목</div>
            <p>모달 내용 Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
            <div class="close-wrapper">
                <button id="close">닫기</button>
            </div>
        </div>
    </div>
    `;

    document.body.appendChild(modalWrapper);
    
    // 닫기 이벤트 추가
    // document.getElementById('close').onclick = () => {
    //     modalWrapper.remove();
    // };

    document.getElementById('close').onclick = () => {
        modalWrapper.remove();
    };
};