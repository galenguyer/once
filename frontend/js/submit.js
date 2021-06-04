const url = "http://localhost:5000/api/v1/secrets/"

async function submit() {
    const data = "test data for now - we'll get there".trim();
    const hash = getIdFromHash(await hashText(data));
    const request = new Request(url + hash, {
        method: 'POST',
        body: JSON.stringify({data: data}),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    });
    
    fetch(request)
    .then(res => res.json())
    .then(res => {
        console.log("returned id: ", res.id);
    })
}

function generateKey(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}
 