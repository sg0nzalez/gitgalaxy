package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "WS_PRESTAMO")
public class WsPrestamo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_NOMBRE")
    private String wsNombre;

    @Column(name = "WS_ID")
    private Integer wsId;

    @Column(name = "WS_DIRECCION")
    private String wsDireccion;

    @Column(name = "WS_NUMERO")
    private String wsNumero;

    @Column(name = "WS_CIUDAD")
    private String wsCiudad;

    @Column(name = "WS_POSTAL")
    private String wsPostal;

    @Column(name = "WS_CAPITAL")
    private BigDecimal wsCapital;

    @Column(name = "WS_INTERES")
    private BigDecimal wsInteres;

    @Column(name = "WS_FACTOR")
    private BigDecimal wsFactor;

}