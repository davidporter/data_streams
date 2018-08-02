var bardata = [20, 30, 45, 15, 34, 55, 20, 11, 44]
var height = 400,
    width = 600,
    barWidth = 50,
    barOffset = 5;  // space in between bars

var yScale = d3.scaleLinear() // a new array of data - scaled
    .domain([0, d3.max(bardata)])
    .range([0, height]);


d3.select("body").append("p").text("Temperature of floors in home compared to outside"); // canNOT select svg to append a p tag

d3.select('#viz').append('svg')
  .attr('width', width)
  .attr('height', height)
  .style('background', '#C9D7D6')
.selectAll('rect').data(bardata)  // we are selecting the 'rect' rectangles before they actually exist
  .enter().append('rect')  // the rectangle must be appended  ? what is .enter()
    .style('fill', '#C61C6F')
    .attr('width', barWidth)
    .attr('height', function(d) {  // set the height equal to d
        console.log(d);
        console.log(yScale(d));
        return yScale(d);
        
    })
    .attr('x', function(d, i) {
        return i*(barWidth + barOffset)
    })
    .attr('y', function(d) {
        return height - yScale(d);
    });



