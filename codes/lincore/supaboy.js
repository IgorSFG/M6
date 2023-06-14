import { createClient } from '@supabase/supabase-js'

const url = "https://etxrmfvkgcrpyzdpvvrn.supabase.co"
const key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV0eHJtZnZrZ2NycHl6ZHB2dnJuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjY4MDk4MCwiZXhwIjoyMDAyMjU2OTgwfQ.BosLYjeNsyNMhs88FlV_PNzH9QRBqeBgAUJJU4SzlQw"
const supabase = createClient(url, key)

const table = "Coordinates"

async function insertinTable(x, y, theta) {
    
    const {data, error} = await supabase
    .from(table)
    .insert({"x": x, "y": y, "theta": theta})

}

async function deleteinTable() {
    
    const {data, error} = await supabase
    .from(table)
    .delete()

}