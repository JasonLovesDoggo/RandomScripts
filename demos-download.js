// Get the current state from Calc
const state = Calc.getState();

// Create a string with date and expressions
const expressionText = new Date() + "\n" + 
    state.expressions.list.map(x => {
        let y = JSON.stringify(x.latex);
        y = y ? y : '';
        return y.substring(1, y.length - 1);
    }).join('\n');

// Download the expressions as a text file
download(expressionText, "expressions.txt", "text/plain; charset=UTF-8");

// Function to handle file downloads
function download(data, filename, type) {
    var file = new Blob([data], {type: type});
    
    if (window.navigator.msSaveOrOpenBlob) {
        // For IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    } else {
        // For other browsers
        var a = document.createElement("a");
        var url = URL.createObjectURL(file);
        
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
}
