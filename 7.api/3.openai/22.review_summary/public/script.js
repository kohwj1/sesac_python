async function submitReview() {
    const rating = document.querySelector('input[name="rating"]:checked')
    const opinion = document.getElementById('opinion')

    if (!rating || !opinion.value.trim()) {
        alert('평점 또는 후기를 작성해주세요.');
        return;
    }

    const review = {
        rating: rating.value,
        opinion: opinion.value
    }

    try {
        res = await fetch('/api/review', {
            method: 'POST',
            headers: {'Content-Type': 'application/json; charset=UTF-8'},
            body: JSON.stringify(review)
        })

        if (!res.ok) {
            throw new Error;
        }

        get_reviews()
        opinion.value = ''
    }
    catch {
        console.log(Error)
    }
}

async function get_reviews() {
    const res = await fetch('/api/reviewes');
    const resjson = await res.json();
    let review_list = await resjson.data;
    review_list.reverse();
    // console.log(review_list)
    dispalyReview(review_list);
    fetchcAISummary();
}

function dispalyReview(review_list) {
    const user_review = document.getElementById('user-review');
    user_review.innerHTML = '';
    for (item of review_list) {
        review_box = document.createElement('div')
        review_box.textContent = `${item.rating}점 | ${item.opinion}`
        review_box.classList.add('review-box')
        user_review.appendChild(review_box)
    }
}

async function fetchcAISummary() {
    const lang = document.getElementById('langSelect').value;
    const res = await fetch(`/api/ai-summary?lang=${lang}`)
    const data = await res.json();
    console.log(data);
    displayAISummary(data);
}

function displayAISummary(data) {
    const summaryBox = document.querySelector('.ai-summary')
    summaryBox.innerHTML = `
                    <p><strong>AI 요약 | </strong>${data.summary}</p>
                    <p><strong>별점 평균 | </strong>${data.averageRating.toFixed(2)}</p>
    `
}

document.addEventListener('DOMContentLoaded', async(e) => {
        get_reviews();
        fetchcAISummary();
    }
)

document.getElementById('langSelect').addEventListener('change', fetchcAISummary())