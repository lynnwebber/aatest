/*
  a simple restful server
 */
 package main

 import (
     "log"
     "fmt"
     "database/sql"
     _"github.com/lib/pq"
 )

 func main() {
    db,err := sql.Open("postgres","user=lynn dbname=lynn sslmode=disable")
    if err != nil {
        log.Fatal(err)
    }

    rows,err := db.Query("SELECT rtu_channel_id,version,status,attributes_json from rtu_channels")
    if err != nil {
        log.Fatal(err)
    }

    for rows.Next() {
        var chann string
        var ver string
        var status string
        var json string
        err = rows.Scan(&chann,&ver,&status,&json)
        if err != nil {
            log.Fatal(err)
        }
        fmt.Printf("%s\n",chann)
    }

 }
