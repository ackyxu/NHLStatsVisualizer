const yearButton = document.getElementById("yearButton")
const teamButton = document.getElementById("teamButton")
const playerButton = document.getElementById("playerButton")
const reportButton = document.getElementById("reportButton")

window.onload = async() => {
	const yearlist = await eel.queryYearsDB()();
	const yearDropdown = document.getElementById("yeartobeselected");
	if (yearlist.length == 0){
		yearDropdown.innerHTML=`<option> Error: No Years Found </option>`;
	} else {
		for (const year of yearlist){
			yearDropdown.innerHTML+=`<option value=${year}>${year}</option>`;
		}
	}
}


yearButton.addEventListener('click', async() => {
	const teamsDropdown = document.getElementById("teamList")
	const year = document.getElementById("yeartobeselected").value;
	const teamList = await eel.queryTeamsByYear(year)()
	if (teamList.length === 0){
		teamsDropdown.innerHTML = `<option> Error: No Teams Found From the Selected Year</option>`
	} else {
		teamsDropdown.innerHTML = ``
		for(const team of teamList){
			teamsDropdown.innerHTML += `<option value=${team["id"]}>${team["locationName"]} ${team["teamName"]}</option>`
		}
		
	}

})

teamButton.addEventListener('click', async() => {
	const rosterDropdown = document.getElementById("rosterList")
	const year = document.getElementById("yeartobeselected").value;
	const team = document.getElementById("teamList").value;
	const rosterList = await eel.queryTeamRosterByYear(year,team)()
	if (rosterList.length === 0){
		rosterDropdown.innerHTML = `<option> Error: No Player Found From The Team/Year Selected</option>`
	} else {
		rosterDropdown.innerHTML = ``
		for(const player of rosterList){
			rosterDropdown.innerHTML += `<option value=${player["id"]}>${player["firstname"]} ${player["lastname"]}</option>`
		}
		
	}

})

playerButton.addEventListener('click', async() => {
	const year = document.getElementById("yeartobeselected");
	const team = document.getElementById("teamList");
	const player = document.getElementById("rosterList");

	const yearVal = year.options[year.selectedIndex].text;
	const teamVal = team.options[team.selectedIndex].text;
	const playerVal = player.options[player.selectedIndex].text;

	document.getElementById("confirmation").style.display = "block";
	const playerConfirm = document.getElementById("confirmationPlayer")

	playerConfirm.innerHTML = `${yearVal} ${teamVal} ${playerVal}`;

})

reportButton.addEventListener('click', async() => {
	const year = document.getElementById("yeartobeselected").value;
	// const team = document.getElementById("teamList").value;
	const player = document.getElementById("rosterList").value;

	await eel.createFowardReportCard(year,player)();

})