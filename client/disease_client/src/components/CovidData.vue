<template>

    <div v-if="countries.length > 0">

    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Covid Tracker</a>
            <button class="navbar-toggler" type="button" data-coreui-toggle="collapse"
                data-coreui-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link disabled">{{ currentDateTime() }}</a>
                    </li>
                </ul>



                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 px-3">
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Data updated:
                            {{ getDateTime(covidData.updated) }}</a>
                    </li>
                </ul>
                <div class="country_container" style="margin-right: 1rem">
                    <div class="country_content">
                        <select name="country_select" id="" @change="updateData($event)" class="form-select form-control" style="mr-3">
                            <option v-for="country in countries" :key="country.iso_code" :selected="country.iso_code == 'ie'">
                                {{ country.name }}
                            </option>
                        </select>

                    </div>
                </div>

                <button class="btn btn-success update-button px-3" alt='updates covid data in db to latest available' type="submit"
                    v-on:click="updateDb()" id="updateButton">Update</button>
            </div>
        </div>
    </nav>


    <div v-if="covidData.country" class="container-fluid">
        <div class="row">
            <div class="col-3 align-self-start">
                <!-- Mandatory Stats -->
                <div class="card border-0" style="width: 24rem; height: 30rem;">
                    <img v-bind:src="covidData.countryInfo.flag" class="card-img-top" alt="..." >
                    <div class="card-body">
                        <h5 class="card-title">{{ covidData.country }}</h5>
                        <div class="container">
                            <div class="row">
                                <div class="col"><b>Population:</b></div>
                                <div class="col">{{ covidData.population.toLocaleString() }}</div>
                            </div>
                            <div class="row">
                            </div>
                            <div class="row">
                                <div class="col"><b>Cases:</b></div>
                                <div class="col">{{ covidData.cases.toLocaleString() }}</div>
                            </div>
                            <div class="row">
                                <div class="col"><b>Deaths:</b></div>
                                <div class="col">{{ covidData.deaths.toLocaleString() }}</div>
                            </div>
                            <div class="row">
                                <div class="col"><b>Recovered:</b></div>
                                <div class="col">{{ covidData.recovered.toLocaleString() }}</div>
                            </div>
                            <div class="row">
                                <div class="col"><b>Tests:</b></div>
                                <div class="col">{{ covidData.tests.toLocaleString() }}</div>
                            </div>
                            <div class="row">
                                <div class="col"><b>Active:</b></div>
                                <div class="col">{{ covidData.active.toLocaleString() }}</div>
                            </div>
                            <div class="row">
                                <div class="col"><b>Critical:</b></div>
                                <div class="col">{{ covidData.critical.toLocaleString() }}</div>
                            </div>

                            <div class="row my-3">
                                <div class="col">
                                        <a :href="getMapLink()" target="_blank" class="btn btn-primary">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                            fill="currentColor" class="bi bi-map" viewBox="0 0 16 16">
                                            <path fill-rule="evenodd"
                                                d="M15.817.113A.5.5 0 0 1 16 .5v14a.5.5 0 0 1-.402.49l-5 1a.502.502 0 0 1-.196 0L5.5 15.01l-4.902.98A.5.5 0 0 1 0 15.5v-14a.5.5 0 0 1 .402-.49l5-1a.5.5 0 0 1 .196 0L10.5.99l4.902-.98a.5.5 0 0 1 .415.103zM10 1.91l-4-.8v12.98l4 .8V1.91zm1 12.98 4-.8V1.11l-4 .8v12.98zm-6-.8V1.11l-4 .8v12.98l4-.8z">
                                            </path>
                                        </svg>
                                    </a>
                                </div>
                                <div class="col">
                                    <a :href="getMapLink(true)" target="_blank" class="btn btn-primary">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                            fill="currentColor" class="bi bi-virus" viewBox="0 0 16 16">
                                            <path fill-rule="evenodd"
                                                d="M8 0a1 1 0 0 1 1 1v1.402c0 .511.677.693.933.25l.7-1.214a1 1 0 0 1 1.733 1l-.701 1.214c-.256.443.24.939.683.683l1.214-.701a1 1 0 0 1 1 1.732l-1.214.701c-.443.256-.262.933.25.933H15a1 1 0 1 1 0 2h-1.402c-.512 0-.693.677-.25.933l1.214.701a1 1 0 1 1-1 1.732l-1.214-.7c-.443-.257-.939.24-.683.682l.701 1.214a1 1 0 1 1-1.732 1l-.701-1.214c-.256-.443-.933-.262-.933.25V15a1 1 0 1 1-2 0v-1.402c0-.512-.677-.693-.933-.25l-.701 1.214a1 1 0 0 1-1.732-1l.7-1.214c.257-.443-.24-.939-.682-.683l-1.214.701a1 1 0 1 1-1-1.732l1.214-.701c.443-.256.261-.933-.25-.933H1a1 1 0 1 1 0-2h1.402c.511 0 .693-.677.25-.933l-1.214-.701a1 1 0 1 1 1-1.732l1.214.701c.443.256.939-.24.683-.683l-.701-1.214a1 1 0 0 1 1.732-1l.701 1.214c.256.443.933.261.933-.25V1a1 1 0 0 1 1-1Zm2 5a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM6 7a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm1 4a1 1 0 1 0 0-2 1 1 0 0 0 0 2Zm5-3a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z">
                                            </path>
                                        </svg>
                                    </a>
                                </div>
                            </div>


                        </div>
                    </div>
                </div>
            </div>
            <div class="col-9">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col">
                            <!-- Extras -->
                            <div class="container-fluid">
                                <div class="row">
                                    <div class="col">
                                        <div class="card border-0" style="width: 48rem; height: 15rem;">
                                            <div class="card-body">
                                                <h5 class="card-title">Daily</h5>
                                                <div class="container">
                                                    <div class="row">
                                                        <div class="col"><b>Cases:</b></div>
                                                        <div class="col">{{ covidData.todayCases.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Deaths:</b></div>
                                                        <div class="col">{{ covidData.todayDeaths.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Recovered:</b></div>
                                                        <div class="col">{{ covidData.todayRecovered.toLocaleString() }}</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </div>

                                    </div>

                                </div>

                                <div class="row">
                                    <div class="col">
                                        <div class="card border-0" style="width: 48rem; height: 15rem;">
                                            <div class="card-body">
                                                <h5 class="card-title">Per People</h5>
                                                <div class="container">
                                                    <div class="row">
                                                        <div class="col"><b>Case:</b></div>
                                                        <div class="col">{{ covidData.oneCasePerPeople.toLocaleString() }}
                                                        </div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Death:</b></div>
                                                        <div class="col">{{ covidData.oneDeathPerPeople.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Test:</b></div>
                                                        <div class="col">{{ covidData.oneTestPerPeople.toLocaleString() }}</div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                    </div>

                                </div>
                                <div class="row">
                                    <div class="col">
                                        <div class="card border-0" style="width: 48rem; height: 15rem;">
                                            <div class="card-body">
                                                <h5 class="card-title">Per Million</h5>
                                                <div class="container">
                                                    <div class="row">
                                                        <div class="col"><b>Cases:</b></div>
                                                        <div class="col">{{ covidData.casesPerOneMillion.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Deaths:</b></div>
                                                        <div class="col">{{ covidData.deathsPerOneMillion.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Recovered:</b></div>
                                                        <div class="col">{{ covidData.recoveredPerOneMillion.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Tests:</b></div>
                                                        <div class="col">{{ covidData.testsPerOneMillion.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Active:</b></div>
                                                        <div class="col">{{ covidData.activePerOneMillion.toLocaleString() }}</div>
                                                    </div>
                                                    <div class="row">
                                                        <div class="col"><b>Critical:</b></div>
                                                        <div class="col">{{ covidData.criticalPerOneMillion.toLocaleString() }}</div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div v-else class="container-fluid">
    <h1>
        Please press Update Button! <br />
        If you have already, please change country
    </h1>
    </div>

    <nav class="navbar fixed-bottom bg-light" style="height: 3rem;">
        <div class="container-fluid">
            <div class="container-fluid col-3"></div>
            <div class="container-fluid col-3">
                <h5 v-if="this.showMsg">Database updated!</h5>
                <h5 v-else></h5>
            </div>
            <div class="container-fluid col-3"></div>
        </div>
    </nav>

    </div>
    <div v-else>
        <h1>
            Please run script located in: 'res/scripts/add-countries.sql' <br />
            to add countries to database
        </h1>
    </div>
</template>


<script>

export default {
    name: "CovidData",
    components: {
    },
    data() {
        return {
            countries: [''],
            selectedCountry: {},
            covidData: {},
            showMsg: false
        }
    },
    methods: {
        async getCountryData(iso_code = 'ie') {
            try {
                const response = await this.$http.get('http://localhost:8000/api/v1/country');

                this.countries = response.data;
                if (this.countries.length > 0) {
                    try {
                        this.selectedCountry = this.countries.find(country => country.iso_code === iso_code)
                    } catch (error) {
                        this.selectedCountry = this.countries[0]
                    }
                }

            } catch (error) {
                console.log(error);
            }
        },
        async getCovidData() {
            try {
                const response = await this.$http.get('http://localhost:8000/api/v1/data/' + this.selectedCountry.iso_code);
                this.covidData = response.data.data;
            } catch (error) {
                console.log('please add covid data')
                this.covidData = {
                    "updated": 0
                }
            }
            
        },
        updateData(e) {
            var countryName = e.target.value;
            this.selectedCountry = this.countries.find(country => country.name === countryName);
            this.getCovidData();
        },
        updateDb() {
            this.$http.get('http://localhost:8000/disease/info').then(response => {
                if (response.status == 201) {
                    this.getCovidData();
                    this.showMessage();    
                }
            });
        },
        showMessage() {
            console.log("showMessage: true");
            this.showMsg = true;
            setInterval(() => {
                this.showMsg = false;
            }, 5000);
        },
        currentDateTime() {
            const current = new Date();
            // const date = current.getFullYear()+'-'+(current.getMonth()+1)+'-'+current.getDate();
            const date = current.getDate() + ' ' + current.toLocaleString('default', { month: 'long' }).substring(0, 3) + ' ' + current.getFullYear();
            const dateTime = date;
            return dateTime;
        },
        getDateTime(timestamp) {
            var dt = new Date(timestamp)
            const date = dt.getDate() + ' ' + dt.toLocaleString('default', { month: 'long' }).substring(0, 3) + ' ' + dt.getFullYear();
            const time = dt.getHours().toString().padStart(2,'0') + ":" + dt.getMinutes().toString().padStart(2, '0') + ":" + dt.getSeconds().toString().padStart(2,'0');
            const dateTime = date + ' ' + time;
            return dateTime;
        },
        getMapLink(covid=false) {
            var zoom = 7;
            if (this.selectedCountry.iso_code == 'ie') {
                zoom = 8;
            }
            return covid ? 
                "https://www.google.com/maps/@" + this.covidData.countryInfo.lat + "," + this.covidData.countryInfo.long + "," + zoom + "z/data=!5m1!1e7" :
                "http://www.google.com/maps/place/" + this.covidData.country + "/@" + this.covidData.countryInfo.lat + "," + this.covidData.countryInfo.long+ "," + zoom + "z";
        }
    },
    created() {
        this.getCountryData().then(() => {
            this.getCovidData();
        });
    }
}
</script>


