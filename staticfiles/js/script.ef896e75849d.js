new Autocomplete('#search', {

    search : input =>{
        console.log(input)
        const url = `/predictions/search/?autocomplete=${input}`
        return new Promise(resolve =>{
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                resolve(data.data)
            })
        })
    },
    onSubmit : result => {
        window.location.replace(`/predictions/player/${result}`)
    }
})