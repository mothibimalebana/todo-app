import Navbar from "./components/Navbar";

function App() {
return (
<div className="App grid grid-rows-[6.25rem_1fr] row-start-2 h-full">
    <h1>Search</h1>
    <div className="main grid grid-cols-[22.8125rem_1fr]">
        <Navbar/>
        <h1>Tasks</h1>
    </div>
</div>
);
}
export default App;
