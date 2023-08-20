
// Sample data (replace with your actual data)
const numpyArrayX = [];
const numpyArrayY = [];

const margin = { top: 20, right: 20, bottom: 50, left: 50 };
const width = 600 - margin.left - margin.right;
const height = 400 - margin.top - margin.bottom;

d3.csv("../../Datasets/BTC-USD_HBAR-USD_Jan22-Aug23.csv").then(d => {
    d.forEach(e => {
        numpyArrayX.push(e.BTC_Chg);
        numpyArrayY.push(e.HBAR_Chg)
    });

    console.log(numpyArrayX);

    const svg = d3.select("#scatter-plot-container")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    // Scale functions
    const xScale = d3.scaleLinear()
        .domain([0, d3.max(numpyArrayX)])
        .range([0, width]);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(numpyArrayY)])
        .range([height, 0]);

    // Create circles for scatter plot
    svg.selectAll("circle")
        .data(numpyArrayX)
        .enter().append("circle")
        .attr("cx", d => xScale(d))
        .attr("cy", (d, i) => yScale(numpyArrayY[i]))
        .attr("r", 5);
    /*
    // Calculate and draw trend line (linear regression)
    const regression = d3.regressionLinear()
        .x(d => d)
        .y((d, i) => numpyArrayY[i]);
 
    const trendLineData = regression(numpyArrayX);
 
    svg.append("path")
        .datum(trendLineData)
        .attr("class", "trend-line")
        .attr("d", d3.line()
            .x(d => xScale(d[0]))
            .y(d => yScale(d[1]))
        );
 
});
*/