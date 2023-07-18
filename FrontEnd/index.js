async function getRink() {
	const divTasks = document.getElementById('msg')
	divTasks.innerHTML = "Waiting for the rink to populate, might take a while"
	const rinkimg = await eel.CreateRinkGraph()();
	document.getElementById("rink").src=`${rinkimg}`;
	divTasks.innerHTML = "Done";
	getPlayerInfo()
}

async function getPlayerInfo() {
	const location = document.getElementById("playerinfo")
	const playerinfo = await eel.GetPlayerInfo()();
	location.innerHTML = playerinfo;
}

async function getPlayerShots() {
	const totalshots = document.getElementById("totalshots")
	const goals = document.getElementById("totalgoals")
	const shotspct = document.getElementById("shotpct")
	const shotPie = document.getElementById("shotPie")
	
	const results = await eel.PlayerShotStats()()
	
	totalshots.innerHTML = `Total Shots: ${results[0][0]}    `
	goals.innerHTML = `Total Goals: ${results[0][1]}    `
	shotspct.innerHTML = `Shooting Pct: %${(results[0][2]*100).toFixed(2)}`
	shotPie.src=`${results[1]}`
}

async function getDataFromPython() {
	document.getElementById('myele').innerText = await eel.get_data()();
}

document.getElementById("mybtn").addEventListener('click', async() => {
	getRink();
	getPlayerShots()
})


document.getElementById("sendbtn").addEventListener('click', async() => {
	await eel.delete(document.getElementById('taskinp').value)
	getTasks();
})