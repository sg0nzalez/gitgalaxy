package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "WS_FECHA")
public class WsFecha {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_NUM1")
    private Integer wsNum1;

    @Column(name = "WS_OLD")
    private String wsOld;

    @Column(name = "WS_YEAR")
    private String wsYear;

    @Column(name = "WS_MONTH")
    private String wsMonth;

    @Column(name = "WS_DAY")
    private String wsDay;

}