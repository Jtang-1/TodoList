function deleteTask(taskID){
    fetch("/delete", {
        method: 'POST',
        body: JSON.stringify({taskID: taskID})
        // or make function createOptions( 'POST', taskID)
    }).then((_res) => {
        // redirects to /
        window.location.href = '/';
    });

}

function createOptions(method, ID){
    return {
        method: method,
        body: JSON.stringify({taskID: ID})
    }
}