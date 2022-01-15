class CommonJs {
    getSuccessToastOptions() {
        return {
            theme: "bubble",
            position: "top-right",
            duration : 2000
        }
    }
}

export let $CommonJs = new CommonJs();