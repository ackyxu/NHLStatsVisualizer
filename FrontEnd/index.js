async function getRink() {
	const divTasks = document.getElementById(`msg`)
	divTasks.innerHTML = "Waiting for the rink to populate, might take a while"
	const rinkimg = await eel.CreateRinkGraph()();
	document.getElementById("rink").src=`${rinkimg}`;
	divTasks.innerHTML = "Done";
	
}


async function getSSP() {
	const ssp = document.getElementById("ssp")
	const sspImg = await eel.CreateShotSelectionPie()()
	ssp.src=`${sspImg}`
}

async function CreatePercentileGuide() {
	const guideDiv = document.getElementById("guideDiv")
	const guideImg = await eel.CreatePercentileGuide()();

	guideDiv.src=`${guideImg}`
}

async function getPlayerInfo() {
	const playerName = document.getElementById("playerName")
	const playerID = document.getElementById("pid")
	const playerPosition = document.getElementById("position")
	const playerInfoRow1 = document.getElementById("playerInfo1")
	const playerInfoRow2 = document.getElementById("playerInfo2")
	const playerinfo = await eel.GetPlayerInfo()();



	const response = await fetch(`https://statsapi.web.nhl.com/api/v1/people/${playerinfo[1]}`);
	const playerJSON = await (response.json());
	const birthCity = playerJSON["people"][0]["birthCity"];
	let birthStateProvince= playerJSON["people"][0]["birthStateProvince"];
	if (birthStateProvince === undefined){
		birthStateProvince = playerJSON["people"][0]["birthCountry"];
	}
	
	const birthDate = playerJSON["people"][0]["birthDate"];
	const weight = playerJSON["people"][0]["weight"];
	const height = playerJSON["people"][0]["height"];
	const shoots = playerJSON["people"][0]["shootsCatches"];
	
	playerName.innerHTML = playerinfo[0];
	// playerID.innerHTML = playerinfo[1];
	playerPosition.innerHTML = `Postition: ${playerinfo[2]} &emsp; Shoots: ${shoots}`;

	const row1 = `Born: ${birthDate} &emsp; ${birthCity},${birthStateProvince}`
	const row2 = `Weight: ${weight}lbs &emsp; Height: ${height} &emsp; Player ID: ${playerinfo[1]}`
	playerInfoRow1.innerHTML = row1;
	playerInfoRow2.innerHTML = row2;

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
				"<th>Goals Per 60</th>"+
				"<th>Points Per 60</th>"+
				"<th>Shooting%</th>"+
				"<th>ATOI</th>"+
				"</tr>"
	
	const resultsDict = await eel.GetPlayerSeasonSummary()();
	for (const result of resultsDict) {
		console.log(result)
		content += `<tr>`+
		`<td>${result['year']}</td>`+
		`<td>${result['gp']}</td>`+
		`<td>${result['goals']}</td>`+
		`<td>${result['assists']}</td>`+
		`<td>${result['points']}</td>`+
		`<td>${result['shots']}</td>`+
		`<td>${result['Goals_Per_60'].toFixed(2)}</td>`+
		`<td>${result['Points_Per_60'].toFixed(2)}</td>`+
		`<td>${(result['ShootingPct']*100).toFixed(2)}%</td>`+
		`<td>${Math.floor((result['Avg_Time_On_Ice'])/60)}:${Math.floor((result['Avg_Time_On_Ice'])%60)}</td>`+
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
	const graph1 = document.getElementById("dist1")
	const graph2 = document.getElementById("dist2")
	const graph3 = document.getElementById("dist3")
	const graph4 = document.getElementById("dist4")


	const plot1 = await eel.StatsGraph("Goals_Per_60")()
	const plot2 = await eel.StatsGraph("Points_Per_60")()
	const plot3 = await eel.StatsGraph("ShootingPct", alignLeft=true)()
	const plot4 = await eel.StatsGraph("Avg_Time_On_Ice",alignLeft=true)()

	graph1.src=`${plot1}`
	graph2.src=`${plot2}`
	graph3.src=`${plot3}`
	graph4.src=`${plot4}`
	
}

async function getDataFromPython() {
	document.getElementById(`myele`).innerText = await eel.get_data()();
}

window.onload = async() => {
	await GetPlayerSeasonSummary()
	await getPlayerInfo()
	await getNormalDist() 
	await CreatePercentileGuide()
	await getRink();
	await getSSP();
	// getPlayerShots()
	
}


// document.getElementById("sendbtn").addEventListener(`click`, async() => {
// 	await eel.delete(document.getElementById(`taskinp`).value)
// 	getTasks();
// })