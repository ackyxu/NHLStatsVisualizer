async function getRink() {
	const divTasks = document.getElementById(`msg`)
	divTasks.innerHTML = "Waiting for the rink to populate, might take a while"
	const rinkimg = await eel.CreateRinkGraph()();
	document.getElementById("rink").src=`${rinkimg}`;
	divTasks.innerHTML = "Done";
	getPlayerInfo()
}

async function getPlayerInfo() {
	const playerName = document.getElementById("playerName")
	const playerID = document.getElementById("pid")
	const playerPosition = document.getElementById("position")
	const playerinfo = await eel.GetPlayerInfo()();
	playerName.innerHTML = playerinfo[0];
	playerID.innerHTML = playerinfo[1];
	playerPosition.innerHTML = playerinfo[2];
}

async function GetPlayerSeasonSummary() {

	const statsTable = document.getElementById("statsTable")
	var content = "<table>"

	content += "<tr>"+
				"<th>Year</th>"+
				"<th>Game Played</th>"+
				"<th>Goals</th>"+
				"<th>Assists</th>"+
				"<th>Points</th>"+
				"<th>Shots</th>"+
				"<th>Goals Per Game</th>"+
				"<th>Points Per Game</th>"+
				"<th>Shooting%</th>"+
				"</tr>"
	
	const resultsDict = await eel.GetPlayerSeasonSummary()();
	console.log(resultsDict)
	for (const result of resultsDict) {
		console.log(result)
		content += `<tr>`+
		`<td>${result['year']}</td>`+
		`<td>${result['gp']}</td>`+
		`<td>${result['goals']}</td>`+
		`<td>${result['assists']}</td>`+
		`<td>${result['points']}</td>`+
		`<td>${result['shots']}</td>`+
		`<td>${result['GoalsPerGame'].toFixed(2)}</td>`+
		`<td>${result['PointsPerGame'].toFixed(2)}</td>`+
		`<td>${(result['ShootingPct']*100).toFixed(2)}%</td>`+
		"</tr>"
		

	}

	
	content += "</table>"


	statsTable.innerHTML = content
}

// async function getPlayerShots() {
// 	const totalshots = document.getElementById("totalshots")
// 	const goals = document.getElementById("totalgoals")
// 	const shotspct = document.getElementById("shotpct")
// 	// const shotPie = document.getElementById("shotPie")
	
// 	const results = await eel.PlayerShotStats()()
	
// 	totalshots.innerHTML = `Total Shots: ${results[0][0]}    `
// 	goals.innerHTML = `Total Goals: ${results[0][1]}    `
// 	shotspct.innerHTML = `Shooting Pct: ${(results[0][2]*100).toFixed(2)}%`
// 	// shotPie.src=`${results[1]}`
// }

async function getNormalDist() {
	const goalsDist = document.getElementById("dist1")
	const pointsDist = document.getElementById("dist2")
	const dist3 = document.getElementById("dist3")


	const goalsPlot = await eel.NormalDistGraphs("GoalsPerGame")()
	const pointsPlot = await eel.NormalDistGraphs("PointsPerGame")()
	const plot3 = await eel.NormalDistGraphs("ShootingPct")()

	goalsDist.src=`${goalsPlot}`
	pointsDist.src=`${pointsPlot}`
	dist3.src=`${plot3}`
}

async function getDataFromPython() {
	document.getElementById(`myele`).innerText = await eel.get_data()();
}

window.onload = async() => {
	await GetPlayerSeasonSummary() 
	await getRink();
	// getPlayerShots()
	await getNormalDist()
}


// document.getElementById("sendbtn").addEventListener(`click`, async() => {
// 	await eel.delete(document.getElementById(`taskinp`).value)
// 	getTasks();
// })