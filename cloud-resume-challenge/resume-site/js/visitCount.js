const api_url = 'https://yx2mfrveth.execute-api.us-east-1.amazonaws.com/Prod/hello';

async function getCount() {
    let response = await fetch(api_url);
    let data = await response.json();
    let body = JSON.parse(data.body)
    document.getElementById('visit_count').innerHTML = body.visit_count;
    console.log(body.visit_count);
}
getCount();