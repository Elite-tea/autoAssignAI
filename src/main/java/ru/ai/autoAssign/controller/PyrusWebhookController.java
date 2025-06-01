package ru.ai.autoAssign.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/pyrus")
public class PyrusWebhookController {

    private final KafkaTemplate<String, String> kafkaTemplate;

    public PyrusWebhookController(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    @PostMapping("/webhook")
    public ResponseEntity<String> handleWebhook(@RequestBody String rawEvent) {
        // Отправляем сырые данные в Kafka (можно парсить и фильтровать)
        kafkaTemplate.send("pyrus", rawEvent);
        return ResponseEntity.ok("OK");
    }
}