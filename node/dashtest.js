var blessed = require('blessed')
    , contrib = require('blessed-contrib')
    , screen = blessed.screen()

var grid = new contrib.grid({rows: 12, cols: 12, screen: screen})

//grid.set(row,col,rowSpan,colSpan,obj,opts)
var table1 = grid.set(0,0,4,3, contrib.table,
    { keys: true
    , fg: 'white'
    , label: 'poll-proc1'
    , columnSpacing: 3 //in chars
    , columnWidth: [15, 10,] /*in chars*/ })

var table2 = grid.set(0,3,4,3, contrib.table,
    { keys: true
    , fg: 'white'
    , label: 'poll-proc2'
    , columnSpacing: 3 //in chars
    , columnWidth: [15, 10,] /*in chars*/ })


var sample_data =  { headers: ['process', 'status'], data:
    [ ['getSomething', 'RUNNING']
    , ['RWSomething', 'RUNNING']
    , ['RWSomething', 'RUNNING']
    , ['RWSomething', 'RUNNING']
    , ['RWSomething', 'RUNNING']
    , ['RWSomething', 'RUNNING']
    , ['doSomething', 'STOPPED'] ]}



table1.setData(sample_data)
table2.setData(sample_data)

 // table1.setData(
 // { headers: ['process', 'status']
 // , data:
 //    [ ['getSomething', 'RUNNING']
 //    , ['RWSomething', 'RUNNING']
 //    , ['RWSomething', 'RUNNING']
 //    , ['RWSomething', 'RUNNING']
 //    , ['RWSomething', 'RUNNING']
 //    , ['RWSomething', 'RUNNING']
 //    , ['doSomething', 'STOPPED'] ]})





screen.key(['escape', 'q', 'C-c'], function(ch, key) {
 return process.exit(0);
});

screen.render()
