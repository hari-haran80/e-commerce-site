const nodes = document.querySelectorAll(".total");
    const arr = Array.from(nodes);
    const res = arr.reduce((acc, curr) => {
        return acc + Number(curr.textContent); 
    }, 0);
    document.getElementById("length").innerHTML = "Items : " + arr.length
    document.getElementById("net").innerHTML = "Total Price : Rs " + res.toFixed(2);
