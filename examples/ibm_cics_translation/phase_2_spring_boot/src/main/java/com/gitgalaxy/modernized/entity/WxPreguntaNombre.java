package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "WX_PREGUNTA_NOMBRE")
public class WxPreguntaNombre {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WX_ENTRADA")
    private String wxEntrada;

    @Column(name = "WX_RESPUESTA")
    private String wxRespuesta;

    @Column(name = "WX_HOLA")
    private String wxHola;

    @Column(name = "WX_SALUDO")
    private String wxSaludo;

    @Column(name = "WX_RESTO_SALUDO")
    private String wxRestoSaludo;

}