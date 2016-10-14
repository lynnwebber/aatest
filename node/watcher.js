
var
    fs = require('fs')
    , spn = require('child_process').spawn
    , fname = process.argv[2];

if (!fname) {
    throw Error("Please provide a file name to watch");
}

fs.watch(fname, function() {
    //console.log("file: "+fname+ " changed");
    var myls = spn('ls', ['-lh', fname]);
    myls.stdout.pipe(process.stdout);
});

console.log("Watching "+fname+" for changes...");
